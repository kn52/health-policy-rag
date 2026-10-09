
import ResourcePage from "../components/ResourcePage";

export default function Patients() {
  return (
    <ResourcePage
      title="Patients"
      endpoint="/api/patients"
      idField="patient_id"
      fields={[
        { name: "patient_id", label: "Patient ID" },
        { name: "name", label: "Full Name" },
        { name: "age", label: "Age", type: "number" },
        { name: "gender", label: "Gender" },
        { name: "phone", label: "Phone" },
        { name: "email", label: "Email", type: "email", required: false },
      ]}
    />
  );
}
