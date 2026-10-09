
import ResourcePage from "../components/ResourcePage";

export default function Billing() {
  return (
    <ResourcePage
      title="Billing"
      endpoint="/api/billing"
      idField="bill_id"
      fields={[
        { name: "bill_id", label: "Bill ID" },
        { name: "patient_id", label: "Patient ID" },
        { name: "amount", label: "Amount", type: "number" },
        { name: "description", label: "Description" },
        { name: "status", label: "Status", defaultValue: "Pending" },
        { name: "due_date", label: "Due Date", type: "date", required: false },
      ]}
    />
  );
}
