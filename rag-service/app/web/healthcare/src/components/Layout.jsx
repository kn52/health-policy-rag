
import { NavLink, Outlet } from "react-router-dom";

const links = [
  { to: "/", label: "Dashboard", icon: "▦" },
  { to: "/patients", label: "Patients", icon: "♙" },
  { to: "/doctors", label: "Doctors", icon: "✚" },
  { to: "/appointments", label: "Appointments", icon: "▣" },
  { to: "/prescriptions", label: "Prescriptions", icon: "▤" },
  { to: "/billing", label: "Billing", icon: "$" },
];

export default function Layout() {
  return (
    <div className="app-layout">
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-icon">H+</div>
          <div>
            <strong>HealthCare</strong>
            <span>Management Portal</span>
          </div>
        </div>

        <p className="nav-heading">WORKSPACE</p>

        <nav>
          {links.map((link) => (
            <NavLink
              key={link.to}
              to={link.to}
              end={link.to === "/"}
              className={({ isActive }) =>
                `nav-link ${isActive ? "active" : ""}`
              }
            >
              <span className="nav-icon">{link.icon}</span>
              {link.label}
            </NavLink>
          ))}
        </nav>

        <div className="sidebar-footer">
          Healthcare Administration
        </div>
      </aside>

      <main className="main-area">
        <header className="topbar">
          <span>Healthcare Management System</span>
          <span className="connection-status">
            <span className="status-dot" />
            API-connected UI
          </span>
        </header>

        <div className="content">
          <Outlet />
        </div>
      </main>
    </div>
  );
}
