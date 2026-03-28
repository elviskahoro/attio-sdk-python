# PostScimV2UsersResponse

Created


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `schemas`                                                              | List[*str*]                                                            | :heavy_check_mark:                                                     | N/A                                                                    |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `user_name`                                                            | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `name`                                                                 | [models.PostScimV2UsersName](../models/postscimv2usersname.md)         | :heavy_check_mark:                                                     | N/A                                                                    |
| `emails`                                                               | List[[models.PostScimV2UsersEmail](../models/postscimv2usersemail.md)] | :heavy_check_mark:                                                     | N/A                                                                    |
| `roles`                                                                | List[[models.PostScimV2UsersRole](../models/postscimv2usersrole.md)]   | :heavy_check_mark:                                                     | N/A                                                                    |
| `profile_url`                                                          | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |
| `active`                                                               | *bool*                                                                 | :heavy_check_mark:                                                     | N/A                                                                    |
| `meta`                                                                 | [models.PostScimV2UsersMeta](../models/postscimv2usersmeta.md)         | :heavy_check_mark:                                                     | N/A                                                                    |