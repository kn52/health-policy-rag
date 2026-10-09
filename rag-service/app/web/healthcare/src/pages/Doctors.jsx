
import ResourcePage from "../components/ResourcePage";

export default function Doctors() {
  return (
    <ResourcePage
      title="Doctors"
      endpoint="/api/doctors"
      idField="doctor_id"
      fields={[
        { name: "doctor_id", label: "Doctor ID" },
        { name: "name", label: "Full Name" },
        { name: "specialization", label: "Specialization" },
        { name: "phone", label: "Phone" },
        { name: "email", label: "Email", type: "email", required: false },
      ]}
    />
  );
}
