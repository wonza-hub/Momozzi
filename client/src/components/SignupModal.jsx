import { useState, useRef } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const SignupModal = ({ handleSignupOpen }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [age, setAge] = useState(0);
  const [isLoading, setIsLoading] = useState(false);

  const navigate = useNavigate();

  const emailInputRef = useRef();
  const passwordInputRef = useRef();
  const firstNameInputRef = useRef();
  const lastNameInputRef = useRef();
  const ageInputRef = useRef();

  const handleEmailInputChange = () => {
    setEmail(emailInputRef.current.value);
  };
  const handlePasswordInputChange = () => {
    setPassword(passwordInputRef.current.value);
  };
  const handleFirstNameInputChange = () => {
    setFirstName(firstNameInputRef.current.value);
  };
  const handleLastNameInputChange = () => {
    setLastName(lastNameInputRef.current.value);
  };
  const handleAgeInputChange = () => {
    setAge(ageInputRef.current.value);
  };

  const handleSignupSubmit = (event) => {
    event.preventDefault();
    if (!email) {
      return alert("이메일을 입력하세요");
    }
    if (!password) {
      return alert("비밀번호를 입력하세요");
    }
    if (!firstName) {
      return alert("성을 입력하세요");
    }
    if (!lastName) {
      return alert("이름을 입력하세요");
    }
    if (!age) {
      return alert("나이를 입력하세요");
    }

    let body = {
      email,
      password,
      first_name: firstName,
      last_name: lastName,
      age: age,
    };

    // POST: 사용자 회원가입 정보 입력
    const signupPostURL = `${process.env.REACT_APP_SERVER}/api/user/`;
    axios
      ?.post(signupPostURL, body, {
        headers: {
          "Content-Type": "application/json",
        },
      })
      ?.then((res) => {
        if (res.status === 200) {
          navigate("");
          handleSignupOpen();
        }
      })
      ?.catch(() => {
        alert("회원가입 실패");
        setIsLoading(false);
      });
    setIsLoading(true);
  };

  return (
    <>
      <form action="" onSubmit={handleSignupSubmit}>
        <div
          className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[485px] h-[700px] px-4 py-8 bg-white rounded-3xl brightness-95 shadow-[0_8px_30px_rgb(0,0,0,0.12)]"
          onClick={(e) => e.stopPropagation()}
        >
          <div className="w-full h-full flex flex-col items-center">
            <header>
              <h3 className="my-10 text-2xl text-primary tracking-wider">
                MOMOZZI
              </h3>
            </header>
            <div className="w-3/4">
              <div className="mb-2">Email</div>
              <input
                onChange={handleEmailInputChange}
                className="w-full h-12 mb-2 px-8  bg-backgroundGray/50 rounded-lg focus:outline-primary"
                type="text"
                value={email}
                placeholder={"Enter your email"}
                ref={emailInputRef}
              />
              <div className="mb-2">Password</div>
              <input
                onChange={handlePasswordInputChange}
                className="w-full h-12 mb-5 px-8  bg-backgroundGray/50 rounded-lg focus:outline-primary"
                type="password"
                value={password}
                placeholder={"Enter your Password"}
                ref={passwordInputRef}
              />
              <div>
                <span className="mr-4">First Name</span>
                <input
                  onChange={handleFirstNameInputChange}
                  className="w-40 h-12 mb-5 px-8  bg-backgroundGray/50 rounded-lg focus:outline-primary"
                  type="text"
                  value={firstName}
                  placeholder={"FirstName"}
                  ref={firstNameInputRef}
                />
              </div>
              <div>
                <span className="mr-4">Last Name</span>
                <input
                  onChange={handleLastNameInputChange}
                  className="w-40 h-12 mb-5 px-8 bg-backgroundGray/50 rounded-lg focus:outline-primary"
                  type="text"
                  value={lastName}
                  placeholder={"LastName"}
                  ref={lastNameInputRef}
                />
              </div>
              <div>
                <span className="mr-4">Age</span>
                <input
                  onChange={handleAgeInputChange}
                  className="w-2/5 h-12 mb-5 px-8  bg-backgroundGray/50 rounded-lg focus:outline-primary"
                  type="number"
                  value={age}
                  placeholder={"Age"}
                  ref={ageInputRef}
                />
              </div>
              <button
                className=" w-full mt-8 h-14 tracking-wider border-2 border-black/80 rounded-3xl"
                disabled={isLoading}
              >
                Complete
              </button>
            </div>
          </div>
        </div>
      </form>
    </>
  );
};

export default SignupModal;
