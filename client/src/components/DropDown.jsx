import { Select, MenuItem } from "@mui/material";
import { useState } from "react";

const DropDown = ({ menuItems, setArg }) => {
  const [item, setItem] = useState(menuItems[0]);

  const handleChange = (event) => {
    setItem(event.target.value);
    setArg(event.target.value);
  };

  return (
    <>
      <Select
        className="w-48 h-8"
        value={item}
        onChange={handleChange}
        renderValue={(value) => (value ? value : "None")}
      >
        {menuItems.map((item, idx) => (
          <MenuItem key={idx} value={item}>
            {item}
          </MenuItem>
        ))}
      </Select>
    </>
  );
};

export default DropDown;
