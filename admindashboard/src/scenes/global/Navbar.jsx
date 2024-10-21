import { useState } from "react";
import { ProSidebar, Menu, MenuItem } from 'react-pro-sidebar';
import "react-pro-sidebar/dist/css/styles.css";
import { Box, IconButton, Typography, useTheme } from '@mui/material';
import { Link } from "react-router-dom";
import { tokens } from "../../theme";
import HomeOutLinedIcon from "@mui/icons-material/HomeOutlined";
import PeopleOutLinedIcon from "@mui/icons-material/PeopleOutlined";
import ContactsOutLinedIcon from "@mui/icons-material/ContactsOutlined";
import ReceiptOutLinedIcon from "@mui/icons-material/ReceiptOutlined";
import PersonOutLinedIcon from "@mui/icons-material/PersonOutlined";
import CalendarTodayOutLinedIcon from "@mui/icons-material/CalendarTodayOutlined";
import HelpOutLinedIcon from "@mui/icons-material/HelpOutlined";
import BarCharOutLinedIcon from "@mui/icons-material/BarChartOutlined";
import PieChartOutlineOutLinedIcon from "@mui/icons-material/PieChartOutlineOutlined";
import TimelineOutLinedIcon from "@mui/icons-material/TimelineOutlined";
import MenuOutLinedIcon from "@mui/icons-material/MenuOutlined";
import MapOutLinedIcon from "@mui/icons-material/MapOutlined";

const Item = ({ title, to, icon, selected, setSelected }) => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    return (
        <MenuItem
            active={selected === title}
            style={{ color: colors.gray[100], }}
            onClick={() => setSelected(title)}
            icon={icon}
        >
            <Typography>{title}</Typography>
            <Link to={to} />
        </MenuItem>
    );
};

const Navbar = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    const [isCollapsed, setIsCollapsed] = useState(false);
    const [selected, setSelected] = useState("Dashboard");

    return (
        <Box
            sx={{
                "& .pro-sidebar-inner": {
                    backgroundColor: `${colors.primary[400]} !important`, //sidebar background color
                },
                "& .pro-icon-wrapper": {
                    backgroundColor: 'transparent !important', //icon background
                },
                "& .pro-inner-item": {
                    padding: "5px 35px 5px 20px !important", //padding for each item
                },
                "& .pro-inner-item:hover": {
                    color: "#868dfb !important", //hover color for items
                },
                "& .pro-menu-item.active": {
                    color: "#6870fa !important", //active item color
                },
            }}
        >
            <ProSidebar collapsed={isCollapsed}>
                <Menu iconShape='square'>
                    {/* logo and menu icon */}
                    <MenuItem
                        onClick={() => setIsCollapsed(!isCollapsed)}
                        icon={isCollapsed ? <MenuOutLinedIcon /> : undefined}
                        style={{
                            margin: "10px 0 20px 0",
                            color: colors.gray[100],
                        }}
                    >
                        {!isCollapsed && (
                            <Box display="flex" justifyContent="space-between" alignItems="center" ml="15px">
                                <Typography variant="h6" color={colors.redAccent[400]}>
                                    Call Issue Analysis System
                                </Typography>
                                <IconButton onClick={() => setIsCollapsed(!isCollapsed)}>
                                    <MenuOutLinedIcon />
                                </IconButton>
                            </Box>
                        )}
                    </MenuItem>

                    {/* user info */}
                    {!isCollapsed && (
                        <Box mb="25px">
                            <Box display="flex" justifyContent="center" alignItems="center">
                                <img
                                    alt='profile-user'
                                    width="100px"
                                    height="100px"
                                    src={"../../assets/cat.png"}
                                    style={{ cursor: "pointer", borderRadius: "50%" }}
                                />
                            </Box>
                            <Box textAlign="center">
                                <Typography variant="h4" color={colors.gray[100]} fontWeight="bold" sx={{ m: "10px 0 0 0" }}>
                                    Meowy Whiskers
                                </Typography>
                                <Typography variant="h6" color={colors.greenAccent[500]}>
                                    CEO FYP Studios
                                </Typography>
                            </Box>
                        </Box>
                    )}

                    {/* menu items */}
                    <Box paddingLeft={isCollapsed ? undefined : "10%"}>
                        <Typography variant="h6" color={colors.gray[300]} sx={{ m: "15px 0 5px 20px" }}>Data</Typography>
                        <Item title='Dashboard' to="/" icon={<HomeOutLinedIcon />} selected={selected} setSelected={setSelected} />
                        <Item title='Manage Team' to="/team" icon={<PeopleOutLinedIcon />} selected={selected} setSelected={setSelected} />
                        <Item title='Contact Information' to="/contacts" icon={<ContactsOutLinedIcon />} selected={selected} setSelected={setSelected} />
                        {/* <Item title='Invoices Balances' to="/invoices" icon={<ReceiptOutLinedIcon />} selected={selected} setSelected={setSelected} /> */}

                        <Typography variant="h6" color={colors.gray[300]} sx={{ m: "15px 0 5px 20px" }}>Pages</Typography>
                        <Item title='Profile Form' to="/form" icon={<PersonOutLinedIcon />} selected={selected} setSelected={setSelected} />
                        <Item title='Calendar' to="/calendar" icon={<CalendarTodayOutLinedIcon />} selected={selected} setSelected={setSelected} />
                        {/* <Item title='FAQ Page' to="/faq" icon={<HelpOutLinedIcon />} selected={selected} setSelected={setSelected} /> */}

                        <Typography variant="h6" color={colors.gray[300]} sx={{ m: "15px 0 5px 20px" }}>Charts</Typography>
                        <Item title='Bar Chart' to="/bar" icon={<BarCharOutLinedIcon />} selected={selected} setSelected={setSelected} />
                        <Item title='Pie Chart' to="/pie" icon={<PieChartOutlineOutLinedIcon />} selected={selected} setSelected={setSelected} />
                        <Item title='Line Chart' to="/line" icon={<TimelineOutLinedIcon />} selected={selected} setSelected={setSelected} />
                        <Item title='World Chart' to="/geography" icon={<MapOutLinedIcon />} selected={selected} setSelected={setSelected} />
                    </Box>
                </Menu>
            </ProSidebar>
        </Box>
    );
};

export default Navbar;