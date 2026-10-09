
import { useEffect, useState } from "react";
import { api } from "../api/api";

export default function ResourcePage({
  title,
  endpoint,
  idField,
  fields,
}) {
  const [records, setRecords] = useState([]);
  const [form, setForm] = useState({});
  const [editingId, setEditingId] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  async function loadRecords() {
    setLoading(true);
    setError("");

    try {
      const data = await api.get(`${endpoint}/`);
      setRecords(Array.isArray(data) ? data : []);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadRecords();
  }, [endpoint]);

  function resetForm() {
    setForm({});
    setEditingId(null);
  }

  function startEdit(record) {
    setEditingId(record.id);
    setForm({
      ...record,
      [idField]: record.id,
    });
  }

  async function handleSubmit(event) {
    event.preventDefault();
    setError("");

    const payload = Object.fromEntries(
      fields
        .filter((field) => field.name !== idField)
        .map((field) => [field.name, form[field.name] ?? field.defaultValue ?? ""])
    );

    try {
      if (editingId !== null) {
        await api.put(
          `${endpoint}/${encodeURIComponent(editingId)}`,
          payload
        );
      } else {
        await api.post(`${endpoint}/`, {
          ...payload,
          [idField]: form[idField],
        });
      }

      resetForm();
      await loadRecords();
    } catch (err) {
      setError(err.message);
    }
  }

  async function handleDelete(id) {
    if (!window.confirm(`Delete this ${title.toLowerCase()} record?`)) {
      return;
    }

    setError("");

    try {
      await api.delete(`${endpoint}/${encodeURIComponent(id)}`);
      await loadRecords();
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <section className="page">
      <div className="page-heading">
        <div>
          <h1>{title}</h1>
          <p>Manage {title.toLowerCase()} records</p>
        </div>
        <span className="record-count">{records.length} records</span>
      </div>

      {error && <div className="error">{error}</div>}

      <form className="panel form-grid" onSubmit={handleSubmit}>
        <h2 className="form-title">
          {editingId !== null ? `Edit ${title}` : `Add ${title}`}
        </h2>

        {fields.map((field) => (
          <label className="field" key={field.name}>
            <span>{field.label}</span>
            <input
              type={field.type || "text"}
              value={form[field.name] ?? field.defaultValue ?? ""}
              onChange={(event) =>
                setForm({ ...form, [field.name]: event.target.value })
              }
              required={field.required !== false}
              disabled={editingId !== null && field.name === idField}
            />
          </label>
        ))}

        <div className="form-actions">
          <button className="primary-button" type="submit">
            {editingId !== null ? "Save Changes" : "Add Record"}
          </button>
          {editingId !== null && (
            <button
              className="secondary-button"
              type="button"
              onClick={resetForm}
            >
              Cancel
            </button>
          )}
        </div>
      </form>

      <div className="panel table-panel">
        <h2>All {title}</h2>

        {loading ? (
          <p>Loading records...</p>
        ) : records.length === 0 ? (
          <p className="empty-state">No records found.</p>
        ) : (
          <div className="table-scroll">
            <table>
              <thead>
                <tr>
                  {fields.map((field) => (
                    <th key={field.name}>{field.label}</th>
                  ))}
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {records.map((record) => (
                  <tr key={record.id}>
                    {fields.map((field) => (
                      <td key={field.name}>
                        {String(
                          field.name === idField
                            ? record.id ?? ""
                            : record[field.name] ?? ""
                        )}
                      </td>
                    ))}
                    <td className="actions">
                      <button
                        className="edit-button"
                        onClick={() => startEdit(record)}
                      >
                        Edit
                      </button>
                      <button
                        className="delete-button"
                        onClick={() => handleDelete(record.id)}
                      >
                        Delete
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </section>
  );
}
