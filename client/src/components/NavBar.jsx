import { Outlet, Link } from "react-router-dom";
import { RxHamburgerMenu } from "react-icons/rx";
import { useState } from "react";
import LoginModal from "./LoginModal";
import { clearUser } from "../reducer/userReducer";
import { useSelector, useDispatch } from "react-redux";

const NavBar = () => {
  const [isLoginOpen, setIsLoginOpen] = useState(false);
  const handleLoginOpen = () => {
    setIsLoginOpen(!isLoginOpen);
  };

  const user = useSelector((state) => state.user);
  const userDispatch = useDispatch();

  const handleLogoutClick = () => {
    userDispatch(clearUser());
  };

  return (
    <>
      <div className="fixed w-full h-[100px] px-8 bg-white/95 top-0 z-10 flex flex-row justify-between">
        <h1 className=" my-auto text-4xl font-semibold text-primary">
          <Link to={"/page"}>Momozzi</Link>
        </h1>
        <div className="flex items-center flex-end">
          {user.isLogin ? (
            <>
              <div className="w-12 h-12 mr-6 text-lg text-white text-center leading-[44px] rounded-full bg-secondary">
                {user.name}
              </div>
              <button
                className="text-xl mr-6 px-2 text-black/90"
                onClick={handleLogoutClick}
              >
                Logout
              </button>
            </>
          ) : (
            <button
              className="text-xl mr-6 px-2 text-black/90"
              onClick={handleLoginOpen}
            >
              Login
            </button>
          )}
          <button className="px-2">
            <RxHamburgerMenu className="text-3xl " />
          </button>
        </div>
      </div>
      {isLoginOpen ? (
        <div
          className="fixed t-0 l-0 w-full h-full bg-black/80 z-10"
          onClick={handleLoginOpen}
        >
          <LoginModal handleLoginOpen={handleLoginOpen} />
        </div>
      ) : null}
      <Outlet />
    </>
  );
};

export default NavBar;
