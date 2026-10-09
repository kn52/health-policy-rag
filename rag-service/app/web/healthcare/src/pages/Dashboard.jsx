
import { useEffect, useState } from "react";
import { api } from "../api/api";

const cards = [
  ["total_patients", "Total Patients"],
  ["total_doctors", "Total Doctors"],
  ["total_appointments", "Appointments"],
  ["total_prescriptions", "Prescriptions"],
  ["total_bills", "Total Bills"],
  ["pending_bills", "Pending Bills"],
];

export default function Dashboard() {
  const [data, setData] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    api.get("/api/dashboard/")
      .then(setData)
      .catch((err) => setError(err.message));
  }, []);

  return (
    <section className="page">
      <div className="page-heading">
        <div>
          <h1>Dashboard</h1>
          <p>Healthcare management overview</p>
        </div>
      </div>

      {error && <div className="error">{error}</div>}

      {!data && !error ? (
        <p>Loading dashboard...</p>
      ) : (
        <div className="dashboard-grid">
          {cards.map(([key, label]) => (
            <article className="stat-card" key={key}>
              <span>{label}</span>
              <strong>{data?.[key] ?? 0}</strong>
            </article>
          ))}
        </div>
      )}
    </section>
  );
}
