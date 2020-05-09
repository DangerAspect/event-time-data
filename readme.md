# event-time-data

This repository contains the data JSON files used for the [DA/Siege Event Time converter](https://siege.dangeraspect.xyz/event-time#Y5S1). 

## Private use only

⚠ **This repository is for use by trusted collaborators only.** To use the Event Time Converter as a public user, use the [editor here](https://siege.dangeraspect.xyz/event-time/editor).

## How it works


The name of the file is the alias used in the Event Time Converter. 

For example, data/**Y5S1**.json` can be viewed using [https://siege.dangeraspect.xyz/event-time#Y5S1](https://siege.dangeraspect.xyz/event-time#**Y5S1**). 

## Adding a new event

1. Use [the editor](https://siege.dangeraspect.xyz/event-time/editor) to enter event details. 
2. After entering the details, **right**-click the `Generate link` button. A hidden `Generate JSON` button should appear below. 
3. Click on the new button to get the event in JSON form, along with a handy link to create a new file in this repository.
4. Clicking on the link should open GitHub directly to the new file page. Name the file `<event alias>.json` (e.g. `Y5S1.json`), and paste the JSON contents in.
5. Commit the new file directly to `master`, and check if it works. You can edit the created file later.

## Additional features

In addition to what's allowed in the editor, you can also add a description, and separators in the schedule. See below for an annotated example:

```json
{
    "eventName": "Example event",
    "venueTime": "2020-09-05T08:45",
    // DESCRIPTION: You can add a description field with HTML here.
    "description": "This is an example event. <a href='https://github.com/DangerAspect/event-time-data' target='_blank'>HTML is allowed</a>.",
    "timeZone": "Asia/Singapore",
    "schedule": [
        {
            "name": "Item 1",
            "venueTime": "2020-03-10T09:00"
        },
        {
            "name": "Item 2 (with separator below)",
            "venueTime": "2020-03-10T10:00"
        },
        // SEPARATOR: You can also add separators to visually 
        // break up the schedule into smaller chunks.
        {
            "separator": true
        }
        {
            "name": "Item 3 (notice the space above?)",
            "venueTime": "2020-03-10T11:00"
        }
    ]
}
```