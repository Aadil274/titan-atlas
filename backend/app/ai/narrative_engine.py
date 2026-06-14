def generate_narrative(simulation):

    timeline = simulation["timeline"]

    day_0 = timeline.get("day_0", [])
    day_7 = timeline.get("day_7", [])
    day_30 = timeline.get("day_30", [])

    source = simulation["source"]

    story = [
        f"A disruption at {source} triggers downstream effects."
    ]

    if day_0:
        story.append(
            f"A disruption first impacts {', '.join(day_0)}."
        )

    if day_7:
        story.append(
            f"Within one week {', '.join(day_7)} are affected."
        )

    if day_30:
        story.append(
            f"Within one month {', '.join(day_30)} experience downstream impacts."
        )

    return " ".join(story)