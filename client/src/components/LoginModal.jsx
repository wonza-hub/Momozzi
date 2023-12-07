import { useState, useRef } from "react";
import { useDispatch } from "react-redux";
import axios from "axios";
import { loginUser } from "../reducer/userReducer";
import { useNavigate } from "react-router-dom";

/**
 * 로그인 모달창 컴포넌트
 * @param {handleLoginOpen}
 * @returns
 */
const LoginModal = ({ handleLoginOpen }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const emailInputRef = useRef();
  const passwordInputRef = useRef();

  const userDispatch = useDispatch();
  const navigate = useNavigate();

  const handleEmailInputChange = () => {
    setEmail(emailInputRef.current.value);
  };
  const handlePasswordInputChange = () => {
    setPassword(passwordInputRef.current.value);
  };

  const handleLoginSubmit = (event) => {
    event.preventDefault();
    if (!email) {
      return alert("이메일을 입력하세요");
    }
    if (!password) {
      return alert("비밀번호를 입력하세요");
    }

    let body = {
      email,
      password,
    };

    // POST: 사용자 로그인 정보 입력
    const loginPostURL = `${process.env.REACT_APP_SERVER}/api/user/login/`;
    axios
      ?.post(loginPostURL, body, {
        headers: {
          "Content-Type": "application/json",
        },
      })
      ?.then((res) => {
        if (res.status === 200) {
          userDispatch(loginUser(res.data));
          navigate("");
          handleLoginOpen();
        }
      })
      ?.catch((e) => {
        alert("로그인 실패");
        setIsLoading(false);
      });
    setIsLoading(true);
  };

  return (
    <>
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
            <form className="w-full" onSubmit={handleLoginSubmit}>
              <input
                onChange={handleEmailInputChange}
                className="w-full h-12 mb-5 px-8  bg-backgroundGray/50 rounded-lg focus:outline-primary"
                type="text"
                value={email}
                placeholder={"Email"}
                ref={emailInputRef}
              />
              <input
                onChange={handlePasswordInputChange}
                className="w-full h-12 mb-5 px-8  bg-backgroundGray/50 rounded-lg focus:outline-primary"
                type="password"
                value={password}
                placeholder={"Password"}
                ref={passwordInputRef}
              />
              <button
                className="w-full h-12 my-5 bg-primary/90 rounded-md text-white text-lg tracking-wider focus:outline-primary"
                type="submit"
                disabled={isLoading}
              >
                LOGIN
              </button>
            </form>
            <div className="w-full text-center text-black/80">
              login with SNS account
            </div>
            <button className="w-full h-10 my-4 bg-kakao text-black rounded-xl">
              kakao login
            </button>
            <button className=" w-full mt-24 h-14 tracking-wider border-2 border-black/80 rounded-3xl">
              SIGN UP
            </button>
          </div>
        </div>
      </div>
    </>
  );
};

export default LoginModal;
