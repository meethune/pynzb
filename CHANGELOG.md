# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-01-02

### Added
- Python 3 support (3.8+)
- Modern packaging with `pyproject.toml`
- Optional lxml dependency with automatic fallback to ElementTree
- Command-line example script (`example.py`)
- Comprehensive README with installation and usage examples

### Changed
- **BREAKING**: Dropped Python 2 support
- **BREAKING**: Minimum Python version is now 3.8
- API parameter names: `xml` → `nzb` for better semantic clarity
- Updated all imports to use Python 3 conventions
- Improved error handling with null checks
- Modernized packaging (removed `setup.cfg`, simplified `setup.py`)

### Fixed
- Bug in parser method calls
- Added missing null checks for `current_file` in parsing logic
- Encoding issues with XML/NZB file parsing

### Removed
- **BREAKING**: `ExpatNZBParser` - removed as ElementTree is always available in Python 3
- Python 2 compatibility code (`basestring`, `StringIO`, etc.)
- Redundant packaging configuration files

## [0.1.0] - 2009

### Added
- Initial release by Eric Florenzano
- Support for parsing NZB files
- Multiple parser implementations (expat, ElementTree, lxml)
- Basic API for accessing NZB file contents 