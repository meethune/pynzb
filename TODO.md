# TODO: Pre-Release Checklist & Considerations

This document outlines the key considerations and tasks for preparing the first public release (merging python3 branch to master and bumping version to 0.9.0).

## 🚀 Version Strategy Considerations

- **0.9.0 vs 1.0.0**: Currently planning 0.9.0, which signals "nearly stable but not quite 1.0". This is good for gathering user feedback before committing to API stability
- **Semantic Versioning**: Since this is a major rewrite (Python 2→3), consider if 1.0.0 might be more appropriate to signal the fresh start

## 📚 Documentation & Repository Prep

- [x] **README.md**: Already updated with modern examples
- [ ] **Installation instructions**: Verify they work from PyPI (after publishing)
- [x] **License clarity**: BSD-3-Clause is clear
- [ ] **Contributing guidelines**: Consider adding `CONTRIBUTING.md`
- [ ] **Issue templates**: GitHub issue templates for bugs/features

## 🔍 Code Quality Final Checks

- [x] **All tests passing**: Verified
- [ ] **Code coverage**: Consider adding coverage reporting
- [x] **Security scan**: Run `bandit` or similar for security issues
- [ ] **Dependency audit**: Check for vulnerable dependencies

## 🚢 Release Process

- [ ] **Tag strategy**: Decide on `v0.9.0` or `0.9.0` format
- [ ] **Release notes**: GitHub release with changelog content
- [ ] **PyPI publishing**: 
  - [ ] Test on TestPyPI first
  - [ ] Ensure `twine` is configured
  - [ ] Consider GitHub Actions for automated publishing

## 🔄 Compatibility & Migration

- [x] **Python version matrix**: Test on Python 3.8-3.13 (as configured in CI)
- [ ] **Migration guide**: Consider adding a section for Python 2 users
- [x] **Deprecation warnings**: None needed since it's a major version jump

## ⚠️ Potential Issues to Address

### Critical:
- [x] **Import path changes**: Verify all import paths work correctly
- [x] **API compatibility**: Document any breaking changes from original
- [x] **Error handling**: Ensure graceful failures with helpful messages

### Nice to Have:
- [ ] **Performance benchmarks**: Compare with original version
- [ ] **Memory usage**: Test with large NZB files
- [ ] **Documentation hosting**: Consider ReadTheDocs or GitHub Pages

## 🔀 Pre-Merge Git Workflow

Recommended sequence:
```bash
git checkout master
git pull origin master
git merge python3  # or rebase if you prefer linear history
git tag v0.9.0
git push origin master --tags
```

## 📦 PyPI Publishing Prep

- [ ] **Test build**: `python -m build` to verify package builds
- [ ] **Test installation**: `pip install dist/pynzb-0.9.0.tar.gz`
- [ ] **TestPyPI first**: Upload to test.pypi.org before production

## 🤔 Questions to Consider

1. **Branch strategy**: Do you want to keep both python2 and python3 branches? (for historical reference)
2. **Repository strategy**: Will you maintain the original repo or create a new one? (affects GitHub stars/forks)
3. **Backward compatibility promise**: API stability for future versions?
4. **Support timeline**: How long will you maintain 0.9.x if issues arise?

## ✅ Immediate Actions

- [ ] Run a final comprehensive test on a fresh virtual environment
- [ ] Update version in `pyproject.toml` to `0.9.0`
- [ ] Update CHANGELOG.md date from `2025-01-02` to actual release date
- [ ] Consider adding a `SECURITY.md` file for responsible disclosure

## 🛠️ Additional Tools to Consider

- [ ] **bandit**: Security linting (`pip install bandit && bandit -r pynzb/`)
- [ ] **safety**: Dependency vulnerability checking (`pip install safety && safety check`)
- [ ] **coverage**: Test coverage reporting (`pip install coverage && coverage run -m pytest`)
- [ ] **build**: Package building (`pip install build && python -m build`)
- [ ] **twine**: PyPI uploading (`pip install twine`)

## 📋 Final Pre-Release Verification

- [ ] Fresh virtual environment test
- [ ] All GitHub Actions CI passing
- [ ] Documentation builds correctly
- [ ] Example script works with installed package
- [ ] Import statements work from site-packages
- [ ] No broken links in README/docs
- [ ] Version numbers consistent across all files

---

*This checklist can be updated as tasks are completed or new considerations arise.* 