#!/usrbin/python3
"""0. Creating a Simple Templating Program"""

import os


def generate_invitations(template, attendees):
    """Generates personalized invitation files"""

    if not isinstance(template, str):
        print("Template should be a string !")
        return
    elif not isinstance(attendees, list) or \
            not all(isinstance(attendee, dict) for attendee in attendees):
        print("Attendees should be a list of dictionnaries!")
        return
    elif not template:
        print("Template is empty, no output files generated.")
        return
    elif len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    index = 1

    for attendee in attendees:
        name = attendee.get("name")
        event_title = attendee.get("event_title")
        event_date = attendee.get("event_date")
        event_location = attendee.get("event_location")

        output = template.replace("{name}", name if name else "N/A")
        output = output.replace("{event_title}", event_title if event_title else "N/A")
        output = output.replace("{event_date}", event_date if event_date else "N/A")
        output = output.replace("{event_location}", event_location if event_location else "N/A")

        try:
            with open(f"output_{index}.txt", 'w') as file:
                file.write(output)
        except Exception as err:
            print(f"Error: {err}")

        index += 1
