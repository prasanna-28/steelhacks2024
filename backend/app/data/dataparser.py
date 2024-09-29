from pittapi.courses import *
from pittapi import textbook
import requests

TEXTBOOK_RESOURCE = [
    'https://openstax.org/',
    'https://open.umn.edu/opentextbooks',
    'https://oercommons.org/hubs/open-textbooks',
    'https://libretexts.org'
]

def get_textbook_from_courseid(courseid):
    url = f"https://pitt.verbacompare.com/compare/books?id={courseid}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data and isinstance(data, list):
            return data[0].get('isbn')
        else:
            raise ValueError("Unexpected data format")
    else:
        raise ConnectionError(f"Failed to retrieve data. Status code: {response.status_code}")

def course_to_id(term, subject, course):
    term = _validate_term(term)
    subject = _validate_subject(subject)
    course = _validate_course(course)

    internal_course_id = _get_course_id(subject, course)
    json_response = _get_course_info(internal_course_id)["course_details"]
    json_response_details = _get_course_sections(internal_course_id, term)

    course_title = json_response_details["sections"][0]["descr"]
    course_description = json_response["descrlong"]
    credit_range = (json_response["units_minimum"], json_response["units_maximum"])

    requisites = None
    if "offerings" in json_response and len(json_response["offerings"]) != 0 and "req_group" in json_response["offerings"][0]:
        requisites = json_response["offerings"][0]["req_group"]

    components = None
    if "components" in json_response and len(json_response["components"]) != 0:
        components = [
            Component(
                component=component["descr"],
                required=True if component["optional"] == "N" else False,
            )
            for component in json_response["components"]
        ]

    attributes = None
    if "attributes" in json_response and len(json_response["attributes"]) != 0:
        attributes = [
            Attribute(
                attribute=attribute["crse_attribute"],
                attribute_description=attribute["crse_attribute_descr"],
                value=attribute["crse_attribute_value"],
                value_description=attribute["crse_attribute_value_descr"],
            )
            for attribute in json_response["attributes"]
        ]

    sections = []
    for section in json_response_details["sections"]:
        session = section["session"]
        section_number = section["class_section"]
        class_number = str(section["class_nbr"])
        section_type = section["section_type"]
        status = section["enrl_stat_descr"]

        instructors = None
        if len(section["instructors"]) != 0 and section["instructors"][0] != "To be Announced":
            instructors = [
                Instructor(name=instructor["name"], email=instructor["email"]) for instructor in section["instructors"]
            ]

        meetings = None
        if len(section["meetings"]) != 0:
            meetings = [
                Meeting(
                    days=meeting["days"],
                    start_time=meeting["start_time"],
                    end_time=meeting["end_time"],
                    start_date=meeting["start_dt"],
                    end_date=meeting["end_dt"],
                    instructors=[Instructor(name=meeting["instructor"])],
                )
                for meeting in section["meetings"]
            ]

        sections.append(
            Section(
                term=term,
                session=session,
                section_number=section_number,
                class_number=class_number,
                section_type=section_type,
                status=status,
                instructors=instructors,
                meetings=meetings,
            )
        )

    return CourseDetails(
        course=Course(
            subject_code=subject,
            course_number=course,
            course_id=internal_course_id,
            course_title=course_title,
        ),
        course_description=course_description,
        credit_range=credit_range,
        requisites=requisites,
        components=components,
        attributes=attributes,
        sections=sections,
    )