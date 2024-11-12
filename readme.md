# ClaudeFilePrep: Intelligent File Collector for Claude AI Projects

A powerful Python utility that recursively collects files from nested directories, making it easier to prepare data for AI projects, especially for tools like Claude that require manual file uploads.

## 🎯 Problem It Solves

When working with AI tools like Claude, you often need to upload multiple files for analysis. However, these files might be scattered across different folders and subfolders in your project structure. Manually navigating through directories and uploading files one by one is time-consuming and prone to errors.

This tool automates the process by:

1. Recursively finding all relevant files across nested directories
2. Copying them to a single location (either preserving structure or flattened)
3. Making it easy to upload multiple files at once to Claude or similar platforms

## 🚀 Features

- **Recursive File Collection**: Automatically traverses through all subdirectories
- **Selective Ignoring**: Skip specific folders and file patterns
- **Two Organization Modes**:
  - **Hierarchical**: Preserves original folder structure
  - **Flattened**: Places all files in a single directory with path-encoded names
- **Metadata Preservation**: Maintains file timestamps and permissions
- **Error Handling**: Detailed reporting of successful and failed operations
- **Customizable Separators**: Choose how path components are joined in flattened mode

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/file-collector.git

# Navigate to the directory
cd file-collector

# No additional dependencies required - uses Python standard library!
```

## 🎮 Usage

### Basic Usage

```bash
python file_collector.py source_directory
```

This will copy all files to a `result` directory while preserving the folder structure.

### Flatten Directory Structure

```bash
python file_collector.py source_directory --flatten
```

This will copy all files to a single directory, encoding the path information in the filenames.

### Custom Output Directory

```bash
python file_collector.py source_directory --output-dir my_output
```

### Custom Separator for Flattened Mode

```bash
python file_collector.py source_directory --flatten --separator=-
```

### Python API

You can also use it as a Python module:

```python
from file_collector import copy_files

# Preserve directory structure
copied, failed = copy_files("source_directory")

# Flatten directory structure
copied, failed = copy_files("source_directory", flatten=True)

# Custom configuration
copied, failed = copy_files(
    root_dir="source_directory",
    output_dir="custom_output",
    ignore_folders={'.git', 'node_modules'},
    ignore_patterns={'*.pyc', '*.log'},
    flatten=True,
    separator="-"
)
```

## 🎯 Use Cases

1. **AI Project Data Preparation**
   - Quickly collect all relevant files for uploading to Claude
   - Easily gather training data from multiple directories
   - Prepare datasets for analysis

2. **Project Organization**
   - Consolidate files from complex directory structures
   - Create flat archives of nested projects
   - Prepare files for bulk processing

3. **Backup and Migration**
   - Collect specific file types across directories
   - Create organized backups
   - Prepare files for transfer to different systems

## ⚙️ Configuration

### Ignored Folders (Default)

- `.git`
- `node_modules`
- `__pycache__`

### Ignored File Patterns (Default)

- `*.pyc`
- `*.log`
- `.DS_Store`

## 📝 Example Output

### Directory Structure Example

Let's say you have this project structure:

```bash
my_project/
├── data/
│   ├── raw_data.csv
│   └── processed/
│       ├── cleaned_data.csv
│       └── feature_data.csv
├── notebooks/
│   ├── analysis.ipynb
│   └── visualization.ipynb
├── src/
│   ├── __pycache__/
│   │   └── utils.cpython-39.pyc
│   ├── utils.py
│   └── main.py
└── README.md
```

### Normal Mode Output

Running:

```bash
python file_collector.py my_project
```

Creates:

```
result/
├── data/
│   ├── raw_data.csv
│   └── processed/
│       ├── cleaned_data.csv
│       └── feature_data.csv
├── notebooks/
│   ├── analysis.ipynb
│   └── visualization.ipynb
├── src/
│   ├── utils.py
│   └── main.py
└── README.md
```

Console output:

```bash
Successfully copied files:
✓ data/raw_data.csv
✓ data/processed/cleaned_data.csv
✓ data/processed/feature_data.csv
✓ notebooks/analysis.ipynb
✓ notebooks/visualization.ipynb
✓ src/utils.py
✓ src/main.py
✓ README.md

Total files copied: 8
Total files failed: 0

Files have been copied to: result/
```

### Flattened Mode Output

Running:

```bash
python file_collector.py my_project --flatten
```

Creates:

```
result/
├── data_raw_data.csv
├── data_processed_cleaned_data.csv
├── data_processed_feature_data.csv
├── notebooks_analysis.ipynb
├── notebooks_visualization.ipynb
├── src_utils.py
├── src_main.py
└── README.md
```

Console output:

```
Successfully copied files:
✓ data_raw_data.csv
✓ data_processed_cleaned_data.csv
✓ data_processed_feature_data.csv
✓ notebooks_analysis.ipynb
✓ notebooks_visualization.ipynb
✓ src_utils.py
✓ src_main.py
✓ README.md

Total files copied: 8
Total files failed: 0

Files have been copied to: result/
Directory structure was flattened
```

Note:

- `__pycache__` directory was automatically ignored
- `.pyc` files were skipped based on ignore patterns
- All file metadata (timestamps, permissions) was preserved
- In flattened mode, path separators were converted to underscores

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:

1. Add new features
2. Improve documentation
3. Report bugs
4. Suggest improvements

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

This tool was inspired by the need to streamline file preparation for AI tools like Claude and make data scientists' lives easier.

---

Made with ❤️ to save time and reduce tedious file management tasks.
