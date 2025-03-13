// components/ComparisonTool.jsx
import React from "react";

const ComparisonTool = ({ subscriptions }) => {
  // Filter monthly subscriptions and calculate potential savings
  const monthlySubs = subscriptions.filter(sub => sub.billing_cycle === "monthly");
  let totalSavings = 0;

  monthlySubs.forEach((monthlySub) => {
    // Find corresponding annual plan (if exists)
    const annualSub = subscriptions.find(
      sub => sub.name === monthlySub.name && sub.billing_cycle === "annual"
    );
    if (annualSub) {
      // Savings = (Monthly cost * 12) - Annual cost
      totalSavings += (monthlySub.price * 12) - annualSub.price;
    }
  });

  return (
    <div className="comparison-card">
      <h3>Annual Plan Savings</h3>
      <p>You could save {totalSavings.toFixed(2)} ريال/year!</p>
    </div>
  );
};