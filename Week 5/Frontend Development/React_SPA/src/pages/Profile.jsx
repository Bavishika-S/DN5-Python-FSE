import { useEffect } from "react";

function Profile() {

  useEffect(() => {
    console.log("Profile Loaded");
  }, []);

  return (
    <>
      <h2>Student Profile</h2>
      <p>Name : Bavishika</p>
      <p>Department : CSE</p>
    </>
  );
}

export default Profile;