# Participant


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     | Example                                                         |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `status`                                                        | [models.MeetingStatus](../models/meetingstatus.md)              | :heavy_check_mark:                                              | The status of the individual meeting participant.               | accepted                                                        |
| `is_organizer`                                                  | *bool*                                                          | :heavy_check_mark:                                              | Whether or not the participant is the organizer of the meeting. | false                                                           |
| `email_address`                                                 | *Nullable[str]*                                                 | :heavy_check_mark:                                              | The normalized email address of the meeting participant.        | person@company.com                                              |