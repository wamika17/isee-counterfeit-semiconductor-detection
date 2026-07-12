def analyze_voltage(vin_values, vout_values):

    avg_vin = sum(vin_values) / len(vin_values)
    avg_vout = sum(vout_values) / len(vout_values)

    voltage_drop = avg_vin - avg_vout

    status = "PASS"

    if avg_vout < 4.5:
        status = "FAIL"

    report = {

        "Average Input Voltage": round(avg_vin, 3),

        "Average Output Voltage": round(avg_vout, 3),

        "Voltage Drop": round(voltage_drop, 3),

        "Status": status

    }

    return report


if __name__ == "__main__":

    vin = [5.00, 4.99, 5.01, 5.00]

    vout = [4.98, 4.97, 4.99, 4.98]

    report = analyze_voltage(vin, vout)

    print(report)
