import React from "react";
import { InputField, SelectField } from "../InputFields/InputField";
import { useState } from "react";
import GenericButton from "../Buttons/GenericButton";
import PasswordChecklist from "react-password-checklist";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { storeUserData } from "../../storage-managers/userData";
import { BoxMap } from "../Map";
const backendUrl = import.meta.env.VITE_REACT_BACKEND_URL || ""; //from .env files
const Signup = () => {
  const [name, setName] = useState("");
  const [username, setUsername] = useState("");
  const [phone, setPhone] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [passwordConfirm, setPasswordConfirm] = useState("");
  const [validPassword, setValidPassword] = useState(false);
  const [gender, setGender] = useState(true);
  const [age, setAge] = useState(20);
  const [rent, setRent] = useState(1000000);
  const [locate, setLocate] = useState("");
  const [longtitude, setLongtitude] = useState(105.8333522);
  const [latitude, setLatitude] = useState(21.004);
  const options = [
    { value: true, text: 'Male' },
    { value: false, text: 'Female' },
  ];

  const navigate = useNavigate();
  const HandleSignup = async (e) => {
    e.preventDefault();
    if (!validPassword) {
      alert("Password is not valid");
      return;
    }
    if (name === "" || username === "" || phone === "" || email === "") {
      alert("Please fill in all fields");
      return;
    }
    //TODO: Handle signup
    const signupData = {
      name: name,
      username: username,
      phoneNumber: phone,
      // email: email,
      password: password,
      gender: gender,
      age: age,
      rent: rent,
      // locate: locate,
      longtitude: longtitude,
      latitude: latitude,
    };
    // const formData = new FormData();
    // formData.append("data", JSON.stringify(signupData));
    console.log(signupData);
    const response = await axios.post(`${backendUrl}/roommate/`, signupData);
    if (response.status === 201) {
      console.log(response.data);
      console.log(signupData);
      
      alert("Signup successful, please go to the login page to login");
      navigate("/");
    }

    
  };
  return (
    <div className="select-none bg-[#232831] flex flex-col items-center p-32 gap-32">
      <div className="text-6xl font-extrabold">Sign Up</div>
      <form className="w-1/2 flex flex-col gap-5 items-center">
        <InputField
          type={"text"}
          value={name}
          setValue={setName}
          placeholder={"Full Name"}
        />
        <InputField
          type={"email"}
          value={email}
          setValue={setEmail}
          placeholder={"Email"}
        />
        <InputField
          type={"tel"}
          value={phone}
          setValue={setPhone}
          placeholder={"Phone Number"}
        />
        <SelectField
          value={gender}
          setValue={setGender}
          placeholder="Gender"
          options={options}
        />
        <InputField
          type={"age"}
          value={age}
          setValue={setAge}
          placeholder={"Age"}
        />
        <InputField
          type={"rent"}
          value={rent}
          setValue={setRent}
          placeholder={"Rent"}
        />
        <BoxMap setLongtitude={setLongtitude} setLatitude={setLatitude} setLocate={setLocate} />
        <div className="h-10"></div>
        <InputField
          type={"text"}
          value={username}
          setValue={setUsername}
          placeholder={"Username"}
        />
        <InputField
          type={"password"}
          value={password}
          setValue={setPassword}
          placeholder={"Password"}
        />
        <InputField
          type={"password"}
          value={passwordConfirm}
          setValue={setPasswordConfirm}
          placeholder={"Confirm Password"}
        />
        <PasswordChecklist
          rules={["minLength", "number", "capital", "specialChar", "match"]}
          minLength={8}
          specialChar={true}
          number={true}
          capital={true}
          value={password}
          valueAgain={passwordConfirm}
          messages={{
            minLength: `Password must be ${8} chars minimum.`,
            capital: "Password must contain at least 1 capital letter.",
            number: "Password must contain at least 1 number.",
            specialChar: "Password must contain at least 1 special character.",
            match: "Passwords must match.",
          }}
          onChange={(isValid) => {
            setValidPassword(isValid);
            console.log(isValid);
          }}
        />
        <GenericButton text="Sign Up" onClick={HandleSignup} />
      </form>
    </div>
  );
};

export default Signup;
