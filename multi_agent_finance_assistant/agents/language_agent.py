def generate_market_brief(analysis_summary: dict):
    exposure = analysis_summary
    earnings = exposure["earnings_data"]

    exposure_line = (
        f"Today, your Asia tech allocation is {exposure['current_exposure']}% "
        f"(was {exposure['prev_exposure']}%, {exposure['trend']})."
    )

    earnings_lines = []
    for e in earnings:
        ticker = e["ticker"]
        surprise = e.get("earnings_surprise")
        if surprise is None or str(surprise).lower() == "nan":
            line = f"{ticker} reported earnings, but no surprise data was available."
        else:
            verb = "beat" if float(surprise) > 0 else "missed"
            line = f"{ticker} {verb} estimates by {abs(float(surprise)):.1f}%."

        earnings_lines.append(line)

    sentiment_line = "Regional sentiment is neutral with a cautionary tilt due to rising yields."  # stub

    return "\n".join([exposure_line] + earnings_lines + [sentiment_line])
