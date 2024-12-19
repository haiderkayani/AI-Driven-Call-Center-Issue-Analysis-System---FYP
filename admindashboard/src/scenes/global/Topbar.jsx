import {Box, IconButton, useTheme} from "@mui/material";
import { useContext } from "react";
import { ColorModeContext, tokens } from "../../theme";
import InputBase from "@mui/material/InputBase";
import LightModeOutLinedIcon from "@mui/icons-material/LightModeOutlined";
import DarkModeOutLinedIcon from "@mui/icons-material/DarkModeOutlined";
import SettingsOutLinedIcon from "@mui/icons-material/SettingsOutlined";
import NotificationsOutLinedIcon from "@mui/icons-material/NotificationsOutlined";
import SearchIcon from "@mui/icons-material/Search";
import PersonOutlinedIcon from "@mui/icons-material/PersonOutlined";

const Topbar = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    const colorMode = useContext (ColorModeContext);

    return (<Box display = 'flex' justifyContent="space-between" p={2}> 
        {/* search bar */}
        <Box display="flex" backgroundColor={colors.primary[400]} borderRadius="3px"  sx={{ width: '100%', maxWidth: '1100px' }} >
            <InputBase sx={{ml:2, flex:1}} placeholder="Search" />
            <IconButton type="button" sx={{p:1}}>
                <SearchIcon />
            </IconButton>
        </Box>

        {/* icons */}
        <Box display='flex'>
            <IconButton onClick={colorMode.toggleColorMode}>
                {theme.palette.mode==='dark' ? (
                    <DarkModeOutLinedIcon />
                ) : (
                    <LightModeOutLinedIcon />
                )}
            </IconButton>
            <IconButton><NotificationsOutLinedIcon/></IconButton>
            <IconButton><SettingsOutLinedIcon/></IconButton>
            <IconButton><PersonOutlinedIcon/></IconButton>
        </Box>
    </Box>
    );
};

export default Topbar;