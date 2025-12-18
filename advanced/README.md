# Advanced Python 🚀

Welcome to advanced Python! These concepts will make your code more elegant, efficient, and Pythonic.

## Files in This Section

### 01_decorators.py
**Topics Covered:**
- Function decorators
- Decorators with arguments
- `@functools.wraps`
- Decorator factories
- Multiple decorators
- Class decorators
- Practical decorator examples (timing, caching, validation)

**Key Concepts:**
- Decorators modify function behavior without changing code
- Decorators are functions that take functions as arguments
- `@functools.wraps` preserves function metadata
- Stack decorators for combined effects
- Common uses: logging, timing, caching, validation

**Run it:** `python 01_decorators.py`

### 02_generators.py
**Topics Covered:**
- Generator functions with `yield`
- Generator expressions
- Memory efficiency vs lists
- Infinite generators
- `send()` method
- Generator pipelines
- Practical examples

**Key Concepts:**
- Generators produce values lazily (on-demand)
- Much more memory efficient than lists
- Use `yield` instead of `return`
- Perfect for large datasets or infinite sequences
- Can be chained together in pipelines

**Run it:** `python 02_generators.py`

### 03_context_managers.py
**Topics Covered:**
- The `with` statement
- Creating context managers with classes
- `__enter__` and `__exit__` methods
- `@contextmanager` decorator
- Resource management
- Error handling in context managers
- Multiple context managers

**Key Concepts:**
- Context managers handle setup and cleanup automatically
- Always use `with` for files, locks, connections
- `__enter__` runs at start, `__exit__` runs at end
- `@contextmanager` simplifies creation
- Ensures resources are cleaned up even if errors occur

**Run it:** `python 03_context_managers.py`

## Why These Are "Advanced"

These concepts are "advanced" not because they're hard to use, but because:
1. They require understanding of functions as first-class objects
2. They involve meta-programming (code that modifies code)
3. They optimize performance and resource management
4. They make code more elegant and Pythonic

## When to Use Each

### Decorators
- **Use for**: Cross-cutting concerns (logging, timing, auth)
- **Example**: Adding timing to multiple functions
- **Benefit**: Keeps main logic clean

### Generators
- **Use for**: Large datasets, sequences, streaming data
- **Example**: Processing large files line by line
- **Benefit**: Memory efficiency

### Context Managers
- **Use for**: Resource management (files, locks, connections)
- **Example**: Database connections, file handling
- **Benefit**: Automatic cleanup, exception safety

## Real-World Applications

### Decorators in Practice
```python
# Web frameworks
@app.route('/home')
@login_required
@cache(timeout=300)
def home():
    return render_template('home.html')
```

### Generators in Practice
```python
# Processing large log files
def read_logs(filename):
    with open(filename) as f:
        for line in f:
            yield parse_log_line(line)

# Efficient - doesn't load entire file
for log in read_logs('huge_log.txt'):
    if log.level == 'ERROR':
        process_error(log)
```

### Context Managers in Practice
```python
# Database connection
with database.connection() as conn:
    cursor = conn.cursor()
    cursor.execute(query)
    # Connection auto-closed even if error
```

## Project Ideas

### Decorator Projects
1. **API Rate Limiter**: Limit function calls per time period
2. **Retry Decorator**: Auto-retry failed operations
3. **Performance Profiler**: Track all function calls and times

### Generator Projects
1. **CSV Stream Processor**: Process huge CSV files
2. **Data Pipeline**: Transform data through multiple stages
3. **Web Scraper**: Yield results as they're found

### Context Manager Projects
1. **Database Manager**: Handle connections and transactions
2. **Temporary File Manager**: Create and clean up temp files
3. **Timer Context**: Measure code block execution time

## Common Patterns

### The Decorator Pattern
```python
@functools.wraps(func)
def wrapper(*args, **kwargs):
    # before
    result = func(*args, **kwargs)
    # after
    return result
```

### The Generator Pattern
```python
def generator(iterable):
    for item in iterable:
        # transform
        yield transformed_item
```

### The Context Manager Pattern
```python
@contextmanager
def my_context():
    # setup
    yield resource
    # cleanup
```

## Skills to Master

- [ ] Write custom decorators
- [ ] Use generators for memory efficiency
- [ ] Create context managers for resources
- [ ] Combine these concepts effectively
- [ ] Know when each pattern is appropriate
- [ ] Debug issues with these patterns

## Performance Tips

1. **Decorators**: Minimal overhead if done right
2. **Generators**: Massive memory savings for large data
3. **Context Managers**: Ensure resources are freed properly

## Debugging Advanced Code

- **Decorators**: Check that `@functools.wraps` is used
- **Generators**: Remember they're consumed once
- **Context Managers**: Verify `__exit__` always runs

## Common Pitfalls

### Decorators
- Forgetting `@functools.wraps`
- Not handling `*args, **kwargs`
- Complex nesting making code hard to read

### Generators
- Trying to iterate twice over same generator
- Not realizing when list is needed vs generator
- Forgetting generators are lazy

### Context Managers
- Not handling exceptions in `__exit__`
- Resource leaks if not properly implemented
- Forgetting cleanup code in finally block

## Next Level: Expert Python

After mastering these concepts, explore:
- Metaclasses
- Descriptors
- Async/await and asyncio
- Type hints and mypy
- Performance optimization
- Design patterns
- Testing strategies

## Resources

- [Python Decorators 101](https://realpython.com/primer-on-python-decorators/)
- [Understanding Generators](https://realpython.com/introduction-to-python-generators/)
- [Context Managers](https://realpython.com/python-with-statement/)
- [Python Cookbook (O'Reilly)](https://www.oreilly.com/library/view/python-cookbook-3rd/9781449357337/)

---

**Remember**: Advanced concepts make Python powerful, but use them wisely. Simple is better than complex! ✨
