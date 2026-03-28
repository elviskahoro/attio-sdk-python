# ExternalRefUnion

A consistent external reference used to match and de-duplicate meetings. Can be either a plain string (for external system IDs) or an object with `ical_uid` and `provider`. If you are writing data into Attio which is based upon calendar events that you have synced from a Google or Microsoft calendar, you must use the iCal format to avoid creating duplicate meetings inside Attio.


## Supported Types

### `str`

```python
value: str = /* values here */
```

### `models.ExternalRef`

```python
value: models.ExternalRef = /* values here */
```

