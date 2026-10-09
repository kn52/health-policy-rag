
import ResourcePage from "../components/ResourcePage";

export default function Prescriptions() {
  return (
    <ResourcePage
      title="Prescriptions"
      endpoint="/api/prescriptions"
      idField="prescription_id"
      fields={[
        { name: "prescription_id", label: "Prescription ID" },
        { name: "patient_id", label: "Patient ID" },
        { name: "doctor_id", label: "Doctor ID" },
        { name: "medication", label: "Medication" },
        { name: "dosage", label: "Dosage" },
        { name: "instructions", label: "Instructions", required: false },
      ]}
    />
  );
}
