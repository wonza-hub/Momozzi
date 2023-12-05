import { Outlet, Link } from "react-router-dom";
import { RxHamburgerMenu } from "react-icons/rx";
import { useState, useEffect } from "react";
import LoginModal from "./LoginModal";
import { clearUser } from "../reducer/userReducer";
import { useSelector, useDispatch } from "react-redux";
import axios from "axios";

// 메뉴 드로어 mui
import Box from "@mui/material/Box";
import Drawer from "@mui/material/Drawer";
import Button from "@mui/material/Button";
import List from "@mui/material/List";
import Divider from "@mui/material/Divider";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemText from "@mui/material/ListItemText";

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

  const [state, setState] = useState({
    right: false,
  });

  const toggleDrawer = (anchor, open) => (event) => {
    if (
      event.type === "keydown" &&
      (event.key === "Tab" || event.key === "Shift")
    ) {
      return;
    }

    setState({ ...state, [anchor]: open });
  };

  // 메뉴 드로어 목록
  const list = (anchor) => (
    <Box
      sx={{ width: 250 }}
      role="presentation"
      onClick={toggleDrawer(anchor, false)}
      onKeyDown={toggleDrawer(anchor, false)}
    >
      {/* 로그인 불필요 */}
      <List>
        {[{ search: "레시피 검색" }].map((item, index) => {
          const [key, value] = Object.entries(item)[0];

          return (
            <ListItem key={index} disablePadding>
              <ListItemButton>
                <Link to={key}>
                  <ListItemText primary={value} />
                </Link>
              </ListItemButton>
            </ListItem>
          );
        })}
      </List>
      <Divider />
      {/* 로그인 필요 */}
      {user.isLogin ? (
        <List>
          {[{ mypage: "내 프로필" }].map((item, index) => {
            const [key, value] = Object.entries(item)[0];

            return (
              <ListItem key={index} disablePadding>
                <ListItemButton>
                  <Link to={key}>
                    <ListItemText primary={value} />
                  </Link>
                </ListItemButton>
              </ListItem>
            );
          })}
        </List>
      ) : null}
    </Box>
  );

  return (
    <>
      <div className="fixed w-full h-[100px] px-8 bg-white/95 top-0 z-10 flex flex-row justify-between">
        <h1 className="my-auto text-4xl font-semibold text-primary">
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
            <Button onClick={toggleDrawer("right", true)}>
              <RxHamburgerMenu className="text-3xl" />
            </Button>
            <Drawer
              anchor="right"
              open={state["right"]}
              onClose={toggleDrawer("right", false)}
            >
              {list("right")}
            </Drawer>
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
