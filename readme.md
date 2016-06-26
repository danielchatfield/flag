# flag

A golang inspired simple flag library for python.

## Usage

```python
import flag

num_workers = flag.int("workers", 10, "Number of worker threads")


if __name__ == '__main__':
	flag.parse()

	print("Num workers %d" % num_workers)
```
