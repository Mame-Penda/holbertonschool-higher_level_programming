#!/usr/bin/python3
import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Invalid Input : template must be a string,"
              f"we got {type(template).__name__}")
        return

    if not isinstance(attendees, list) or \
            not all(isinstance(attend, dict) for attend in attendees):
        print("Invalid Input : attendees must be a list of dictionaries,"
              f"we got {type(attendees).__name__}")
        return

    if not template.strip():
        print("Empty Template : Template is empty,"
              "no output files generated.")
        return

    if not attendees:
        print("Empty List of Object: No data provided,"
              "no output files generated.")
        return

    for ind, attendee in enumerate(attendees, start=1):
        msg = template
        try:
            for keys in ["name", "event_title", "event_date",
                         "event_location"]:
                value = attendee.get(keys, "N/A")
                msg = msg.replace(f"{{{keys}}}",
                                  value if value is not None else "N/A")

            out_file = f"output_{ind}.txt"
            if os.path.exists(out_file):
                print(f"The file {out_file} already exists,")
                continue

            with open(out_file, 'w') as invitation:
                invitation.write(msg)

            print(f"The file {out_file} has been generated")

        except Exception as error:
            print("Missing Data in object: "
                  "An error occurred while creating the "
                  f"invitation for {attendee.get('name', 'N/A')}: {error}")
