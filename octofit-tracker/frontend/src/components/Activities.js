import React, { useEffect, useState } from 'react';


function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('https://expert-space-zebra-4vgv99jx6gf7wgp-8000.app.github.dev/api/activities/')
      .then(response => response.json())
      .then(data => setActivities(data))
      .catch(error => console.error('Error fetching activities:', error));
  }, []);

  return (
    <div className="container mt-4">
      <div className="card">
        <div className="card-body">
          <h2 className="card-title mb-4">Activities</h2>
          <div className="table-responsive">
            <table className="table table-striped table-hover">
              <thead className="table-primary">
                <tr>
                  <th>#</th>
                  <th>Name</th>
                </tr>
              </thead>
              <tbody>
                {activities && activities.length > 0 ? activities.map((activity, idx) => (
                  <tr key={idx}>
                    <td>{idx + 1}</td>
                    <td>{activity.name}</td>
                  </tr>
                )) : (
                  <tr><td colSpan="2">No activities found.</td></tr>
                )}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Activities;
