
import ResourcePage from "../components/ResourcePage";

export default function Appointments() {
  return (
    <ResourcePage
      title="Appointments"
      endpoint="/api/appointments"
      idField="appointment_id"
      fields={[
        { name: "appointment_id", label: "Appointment ID" },
        { name: "patient_id", label: "Patient ID" },
        { name: "doctor_id", label: "Doctor ID" },
        { name: "appointment_date", label: "Appointment Date", type: "datetime-local" },
        { name: "reason", label: "Reason" },
        { name: "status", label: "Status", defaultValue: "Scheduled" },
      ]}
    />
  );
}
