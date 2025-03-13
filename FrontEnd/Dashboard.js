// components/Dashboard.jsx
import React, { useContext } from "react";
import { ThemeContext } from "../context/ThemeContext";
import ComparisonTool from "./ComparisonTool";

const Dashboard = ({ subscriptions }) => {
  const { isDark } = useContext(ThemeContext);  // Access theme state

  return (
    <div className={`dashboard ${isDark ? "dark-theme" : "light-theme"}`}>
      <h1>Subscription Dashboard</h1>
      <ComparisonTool subscriptions={subscriptions} />
      {/* Add charts, renewal alerts, etc. */}
    </div>
  );
};