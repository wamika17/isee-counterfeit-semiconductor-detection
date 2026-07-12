
def extract_features(
    ocr_confidence,
    truth_table_accuracy,
    voltage_report,
    failed_logic_tests
):

    features = {

        "OCR Confidence": ocr_confidence,

        "Truth Table Accuracy": truth_table_accuracy,

        "Average Input Voltage":
            voltage_report["Average Input Voltage"],

        "Average Output Voltage":
            voltage_report["Average Output Voltage"],

        "Voltage Drop":
            voltage_report["Voltage Drop"],

        "Failed Logic Tests":
            failed_logic_tests

    }

    return features


if __name__ == "__main__":

    voltage_report = {

        "Average Input Voltage":5.00,

        "Average Output Voltage":4.98,

        "Voltage Drop":0.02,

        "Status":"PASS"

    }

    features = extract_features(

        ocr_confidence=98.6,

        truth_table_accuracy=100,

        voltage_report=voltage_report,

        failed_logic_tests=0

    )

    print(features)
