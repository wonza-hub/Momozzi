import { Outlet, Link } from "react-router-dom";
import { RxHamburgerMenu } from "react-icons/rx";

const NavBar = () => {
  return (
    <>
      <div className="fixed w-full h-[100px] px-8 bg-white/95 top-0 z-10 flex flex-row justify-between">
        <h1 className=" my-auto text-4xl font-semibold text-primary">
          <Link to={"/page"}>Momozzi</Link>
        </h1>
        <div className="flex flex-end">
          <button className="text-xl mr-6 px-2 text-black/90">Login</button>
          <button className="px-2">
            <RxHamburgerMenu className="text-3xl " />
          </button>
        </div>
      </div>
      <Outlet />
    </>
  );
};

export default NavBar;
