# 🎯 Quality Assurance Checklist

Complete checklist for maintaining code quality and best practices.

## 📋 Pre-Commit Checklist

Before committing code, ensure:

### ✅ Code Quality

- [ ] Code is formatted with **Black** (`make format`)
- [ ] Code passes **Ruff** linting (`make lint`)
- [ ] Code passes **mypy** type checking (`make lint`)
- [ ] No commented-out code (unless documented why)
- [ ] No debug print statements
- [ ] No TODO/FIXME without issue number

### ✅ Testing

- [ ] All tests pass (`make test`)
- [ ] New code has tests
- [ ] Test coverage ≥ 75% (`make test-cov`)
- [ ] No skipped tests without reason
- [ ] Tests are deterministic (no random failures)

### ✅ Documentation

- [ ] Public functions have docstrings
- [ ] Docstrings follow Google style
- [ ] README updated if needed
- [ ] CHANGELOG updated (for releases)
- [ ] Type hints on all functions

### ✅ Security

- [ ] No hardcoded secrets/passwords
- [ ] No SQL injection vulnerabilities
- [ ] Input validation present
- [ ] Bandit security scan passes

### ✅ Performance

- [ ] No obvious performance bottlenecks
- [ ] No unnecessary loops
- [ ] Efficient data structures used

## 🚀 Pre-Release Checklist

Before releasing a new version:

### ✅ Version Management

- [ ] Version bumped in `pyproject.toml`
- [ ] Version bumped in `src/speech_to_text_ai/__init__.py`
- [ ] CHANGELOG.md updated
- [ ] Git tag created

### ✅ Testing

- [ ] All tests pass on all supported Python versions (`tox`)
- [ ] Integration tests pass
- [ ] Manual testing completed
- [ ] No known critical bugs

### ✅ Documentation

- [ ] README.md is up-to-date
- [ ] INSTALL.md reflects current installation
- [ ] CLI_USAGE.md documents all commands
- [ ] API documentation generated (if applicable)

### ✅ Build & Distribution

- [ ] Package builds successfully (`hatch build`)
- [ ] Package installs from wheel (`pip install dist/*.whl`)
- [ ] CLI works after installation
- [ ] Dependencies are correct in pyproject.toml

### ✅ GitHub

- [ ] All CI checks pass
- [ ] Pull request approved
- [ ] Branch is up-to-date with main
- [ ] No merge conflicts

## 🔧 Tool-Specific Checks

### Black
```bash
black --check src/ tests/
```
Expected: All files formatted correctly

### Ruff
```bash
ruff check src/ tests/
```
Expected: No linting errors

### Mypy
```bash
mypy src/
```
Expected: No type errors

### Pytest
```bash
pytest --cov=src/speech_to_text_ai --cov-report=term-missing
```
Expected: All tests pass, coverage ≥ 75%

### Bandit
```bash
bandit -r src/
```
Expected: No security issues

### Tox
```bash
tox
```
Expected: All environments pass

## 📊 Coverage Requirements

| Component | Minimum Coverage |
|-----------|-----------------|
| Overall | 75% |
| Core modules | 80% |
| Utils | 70% |
| CLI | 60% |

## 🎨 Code Style Guidelines

### Python Style (PEP 8)
- Line length: 120 characters
- Indentation: 4 spaces
- Quotes: Double quotes for strings
- Imports: Sorted with isort

### Naming Conventions
- Classes: `PascalCase`
- Functions: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Private methods: `_leading_underscore`

### Documentation
- Docstring style: Google
- Type hints: Required
- Comments: Explain "why", not "what"

## 🔍 Review Checklist

For code reviews:

### ✅ Functionality
- [ ] Code does what it's supposed to do
- [ ] Edge cases handled
- [ ] Error handling is appropriate
- [ ] No unnecessary complexity

### ✅ Maintainability
- [ ] Code is readable
- [ ] Functions are small and focused
- [ ] No code duplication
- [ ] Proper separation of concerns

### ✅ Testing
- [ ] Tests are comprehensive
- [ ] Tests are clear and maintainable
- [ ] Mock usage is appropriate
- [ ] Test names are descriptive

### ✅ Performance
- [ ] No unnecessary computations
- [ ] Appropriate data structures
- [ ] Memory usage is reasonable

## 🚨 Red Flags

Immediately fix if you see:

- ⛔ Hardcoded credentials
- ⛔ SQL queries with string concatenation
- ⛔ Disabled security checks
- ⛔ Global mutable state
- ⛔ Circular imports
- ⛔ Unreachable code
- ⛔ Swallowed exceptions

## ✨ Best Practices

Always follow:

1. **DRY** - Don't Repeat Yourself
2. **KISS** - Keep It Simple, Stupid
3. **YAGNI** - You Aren't Gonna Need It
4. **SOLID** principles
5. **Fail fast** - Validate early
6. **Type hints** - Always annotate
7. **Tests first** - TDD when possible

## 📈 Metrics to Track

Monitor these metrics:

| Metric | Target | Tool |
|--------|--------|------|
| Test Coverage | ≥ 75% | pytest-cov |
| Code Complexity | ≤ 10 | ruff (mccabe) |
| Type Coverage | 100% | mypy |
| Security Score | A | bandit |
| Documentation | 100% | interrogate |

## 🎓 Resources

- [PEP 8](https://pep8.org/) - Python Style Guide
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Type Hints](https://docs.python.org/3/library/typing.html)
- [Pytest Best Practices](https://docs.pytest.org/en/stable/goodpractices.html)

## 🔄 Automation

These checks run automatically:

- **Pre-commit hooks** - On every commit
- **CI/CD** - On every push (if configured)
- **Tox** - Before release

Run all checks manually:
```bash
make all
```

---

**Remember:** Quality is not an act, it's a habit! 🎯
