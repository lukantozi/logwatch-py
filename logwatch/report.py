import json

format_line = lambda x: f"Time/date: {x['timestamp']}\nLevel: {x['level']}\nMessage: {x['message']}\n"

def write_report(analyzer, output_file, mode):
    match mode:
        case "text":
            with open(output_file, "w") as f:
                f.write(f"{analyzer.__str__()}\n")
        case "json":
            cbl = analyzer.count_by_level()
            eph = analyzer.errors_per_hour()
            mce = analyzer.most_common_error()
            d = {
                "info": cbl["i"],
                "error": cbl["e"],
                "warning": cbl["w"],
                "most_common_error": mce,
                "errors_per_hour": eph
            }
            json_d = json.dumps(d)
            with open(output_file, "w") as f:
                f.write(f"{json_d}\n")
