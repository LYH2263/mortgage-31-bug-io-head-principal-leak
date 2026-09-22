from app.engines.amortization import equal_payment_schedule


def blended_preview(principal, annual_rate, months, interest_only_rows, preview_rows):
    ep = equal_payment_schedule(principal, annual_rate, months)
    rows = []
    for i in range(min(preview_rows, len(ep["rows"]))):
        if i < len(interest_only_rows):
            io_row = interest_only_rows[i]
            ep_row = ep["rows"][i]
            rows.append({
                **io_row,
                "payment": ep_row["payment"],
                "interest": ep_row["interest"],
            })
        else:
            rows.append(ep["rows"][i])
    return rows
