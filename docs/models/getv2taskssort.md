# GetV2TasksSort

Optionally sort the results. "created_at:asc" returns oldest results first, "created_at:desc" returns the newest results first. If unspecified, defaults to "created_at:asc" (oldest results first).

## Example Usage

```python
from attio.models import GetV2TasksSort
value: GetV2TasksSort = "created_at:asc"
```


## Values

- `"created_at:asc"`
- `"created_at:desc"`
