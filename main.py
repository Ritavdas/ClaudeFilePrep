import os
import shutil
from pathlib import Path
from typing import List, Set, Tuple


def copy_files(
    root_dir: str,
    output_dir: str = "result",
    ignore_folders: Set[str] = None,
    ignore_patterns: Set[str] = None,
    flatten: bool = False,
    separator: str = "_",
) -> Tuple[List[str], List[str]]:
    """
    Recursively copy all files from root_dir to output_dir while ignoring specified folders and patterns.

    Args:
        root_dir (str): The root directory to start searching from
        output_dir (str): The directory where files will be copied to
        ignore_folders (Set[str]): Set of folder names to ignore (e.g., {'.git', 'node_modules'})
        ignore_patterns (Set[str]): Set of patterns to ignore (e.g., {'*.pyc', '*.log'})
        flatten (bool): If True, all files will be copied to the root of output_dir
        separator (str): Character to use when combining path parts in flattened mode

    Returns:
        Tuple[List[str], List[str]]: Lists of (successfully copied files, failed copies)
    """
    if ignore_folders is None:
        ignore_folders = set()
    if ignore_patterns is None:
        ignore_patterns = set()

    root_path = Path(root_dir)
    output_path = Path(output_dir)

    # Create the output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)

    copied_files = []
    failed_copies = []

    try:
        # Walk through directory
        for current_path, dirs, files in os.walk(root_dir):
            # Remove ignored directories
            dirs[:] = [d for d in dirs if d not in ignore_folders]

            # Process files
            for file in files:
                # Skip files matching ignore patterns
                if any(
                    file.endswith(pattern.replace("*", ""))
                    for pattern in ignore_patterns
                ):
                    continue

                # Get source path
                source_path = Path(current_path) / file
                relative_path = source_path.relative_to(root_path)

                try:
                    if flatten:
                        # Create flattened filename by joining path parts
                        path_parts = list(relative_path.parts)
                        flattened_name = separator.join(path_parts)
                        dest_path = output_path / flattened_name
                    else:
                        # Preserve directory structure
                        dest_path = output_path / relative_path
                        dest_path.parent.mkdir(parents=True, exist_ok=True)

                    # Copy the file, preserving metadata
                    shutil.copy2(source_path, dest_path)
                    copied_files.append(str(relative_path))

                except Exception as e:
                    failed_copies.append(f"{relative_path} (Error: {str(e)})")

    except Exception as e:
        print(f"Error accessing directory {root_dir}: {str(e)}")
        return [], []

    return copied_files, failed_copies


# Example usage
if __name__ == "__main__":
    import argparse

    # Set up command line arguments
    parser = argparse.ArgumentParser(description="Copy files with optional flattening")
    parser.add_argument("source_dir", help="Source directory to copy from")
    parser.add_argument(
        "--output-dir", default="result", help="Output directory (default: result)"
    )
    parser.add_argument(
        "--flatten", action="store_true", help="Flatten directory structure"
    )
    parser.add_argument(
        "--separator",
        default="_",
        help="Separator for flattened filenames (default: _)",
    )
    args = parser.parse_args()

    # Define folders and patterns to ignore
    ignore_folders = {".git", "node_modules", "__pycache__", ".next"}
    ignore_patterns = {"*.pyc", "*.log", ".DS_Store", "*.sql", "*.mjs", "*.json"}

    # Copy files
    copied, failed = copy_files(
        args.source_dir,
        args.output_dir,
        ignore_folders=ignore_folders,
        ignore_patterns=ignore_patterns,
        flatten=args.flatten,
        separator=args.separator,
    )

    # Print results
    print("\nSuccessfully copied files:")
    for file in copied:
        print(f"✓ {file}")

    if failed:
        print("\nFailed to copy:")
        for file in failed:
            print(f"✗ {file}")

    print(f"\nTotal files copied: {len(copied)}")
    print(f"Total files failed: {len(failed)}")
    print(f"\nFiles have been copied to: {args.output_dir}/")
    if args.flatten:
        print("Directory structure was flattened")
