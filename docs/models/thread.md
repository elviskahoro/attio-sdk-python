# Thread


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `id`                                                        | [models.ThreadID](../models/threadid.md)                    | :heavy_check_mark:                                          | N/A                                                         |                                                             |
| `comments`                                                  | List[[models.Comment](../models/comment.md)]                | :heavy_check_mark:                                          | An array of comments in the thread, sorted by `created_at`. |                                                             |
| `created_at`                                                | *str*                                                       | :heavy_check_mark:                                          | When the thread was created.                                | 2023-01-01T15:00:00.000000000Z                              |