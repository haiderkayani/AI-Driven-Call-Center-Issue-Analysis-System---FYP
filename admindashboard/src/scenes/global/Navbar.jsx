import { useState } from "react";
import 'react-pro-sidebar/dist/css/styles.css';
import {Sidebar, Menu, MenuItem} from 'react-pro-sidebar';
import {Box, IconButton, Typography, useTheme} from '@mui//material';
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
import { ColorLensRounded } from "@mui/icons-material";

const Item = ({title, to, icon, selected, setSelected}) => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    return(
        <MenuItem active={selected===title} style={{color: colors.grey[100]}} onClick={() => setSelected(title)} icon={icon}>
            <Typography>{title}</Typography>
            <Link to={to}/>
        </MenuItem>
    )
}

const Navbar = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    const [isCollapsed, setIsCollapsed] = useState(false);
    const[selected, setSelected] = useState("Dashboard");

    return (
        <Box
            sx={{
                "& .pro-sidebar-inner":{
                    background: '${colors.primary[400]} !important'
                },
                "& .pro-icon-wrapper":{
                    backgroundColor: 'transparent !important'
                },
                "& .pro-inner-item":{
                    padding: "5px 35px 5px 20px !important"
                },
                "& .pro-inner-item:hover":{
                    color: "#868dfb !important"
                },
                "& .pro-menu-item.active":{
                    color: "#6870fa !important"
                },
            }}
        >
            <Sidebar collapsed={isCollapsed}>
                <Menu iconShape='square'>
                    {/* logo and menu icon */}
                    <MenuItem
                        onClick={() => setIsCollapsed(!isCollapsed)}
                        icon={isCollapsed ? <MenuOutLinedIcon /> : undefined}
                        style={{
                            margin: "10px 0 20px 0",
                            color: colors.grey[100],
                        }}
                    >
                        {!isCollapsed && (
                            <Box display = "flex" justifyContent="space-between" alignItems="center" ml="15px">
                                <Typography variant="h3" color={colors.grey[100]}>
                                    ADMINIS
                                </Typography>
                                <IconButton onClick={() => setIsCollapsed(!isCollapsed)}>
                                    <MenuOutLinedIcon />
                                </IconButton>
                            </Box>
                        )}
                    </MenuItem>

                    {/* user */}
                    {!isCollapsed && (
                        <Box mb="25px">
                            <Box display="flex" justifyContent="center" alignItems="center">
                                <img alt='profile-user' width="100px" height="100px" src={"../../assets/me.png"} style={{cursor:"pointer", borderRadius: "50%"}} />
                            </Box>

                            <Box textAlign="center">
                                <Typography variant="h2" color={colors.grey[100]} fontWeight="bold" sx={{m:"10px 0 0 0"}}>
                                    Haider Ali Kayani
                                </Typography>
                                <Typography variant="h5" color={colors.greenAccent[500]}>
                                    CEO FYP Studios
                                </Typography>
                            </Box>
                        </Box>
                    )}

                    {/* menu items */}
                    <Box paddingLeft={isCollapsed ? undefined : "10%"}>
                        <Item title='Dashbaord' to="/" icon={<HomeOutLinedIcon />} selected={selected} setSelected={setSelected}/>
                        <Item title='Manage Team' to="/tem" icon={<PeopleOutLinedIcon />} selected={selected} setSelected={setSelected}/>
                        <Item title='Contact Information' to="/contacts" icon={<ContactsOutLinedIcon />} selected={selected} setSelected={setSelected}/>
                        <Item title='Invoices Balances' to="/invoices" icon={<ReceiptOutLinedIcon />} selected={selected} setSelected={setSelected}/>
                        <Item title='Profile Form' to="/form" icon={<PersonOutLinedIcon />} selected={selected} setSelected={setSelected}/>
                        <Item title='Calendar' to="/calendar" icon={<CalendarTodayOutLinedIcon />} selected={selected} setSelected={setSelected}/>
                        <Item title='FAQ Page' to="/faq" icon={<HelpOutLinedIcon />} selected={selected} setSelected={setSelected}/>
                        <Item title='Bar Chart' to="/bar" icon={<BarCharOutLinedIcon />} selected={selected} setSelected={setSelected}/>
                        <Item title='Pie Chart' to="/pie" icon={<PieChartOutlineOutLinedIcon />} selected={selected} setSelected={setSelected}/>
                        <Item title='Line Chart' to="/line" icon={<TimelineOutLinedIcon />} selected={selected} setSelected={setSelected}/>
                        <Item title='World Chart' to="/geography" icon={<MapOutLinedIcon />} selected={selected} setSelected={setSelected}/>
                    </Box>
                </Menu>
            </Sidebar>
        </Box>
    )
}

export default Navbar;