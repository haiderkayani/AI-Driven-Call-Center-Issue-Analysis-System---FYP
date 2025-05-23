import { useState } from "react";
import FullCalendar, {formatDate} from "@fullcalendar/react";
import dayGridPlugin from "@fullcalendar/daygrid";
import timeGridPlugin from "@fullcalendar/timegrid";
import listPlugin from "@fullcalendar/list";
import interactionPlugin from "@fullcalendar/interaction";
import {
    Box,
    List,
    ListItem,
    ListItemText,
    Typography,
    useTheme
} from "@mui/material";
import Header from "../../components/Header";
import { tokens } from "../../theme";




const Calendar = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    const [currentEvents, setCurrentEvents] = useState([]);


    const handleDateClick = (selected) => {
        const title = prompt("PLease enter a new title for your event");
        const calendarApi = selected.view.calendar;
        calendarApi.unselect();

        if (title){
            calendarApi.addEvent({
                id : `${selected.dateStr}-${title}`,
                title,
                start: selected.startStr,
                end: selected.endStr,
                allDay: selected.allDay
            });
        }
    };


    const handleEventClick = (selected) => {
        if(window.confirm(`Are you sure you want to delete this event '${selected.event.title}'`)) {
            selected.event.remove();
        }
    };

    return <Box m="20px">
        <Header title="Calendar" subtitle="Full Calendar Interactive Page"/>
        <Box display ="flex" justifyContent="space-between">
            {/*CALENDAT SIDEBAR*/}
            <Box
             flex="1 1 20%" 
             backgroundColor={colors.primary[400]} 
             p="15px" 
             borderRadius="4px"
            >
                <Typography variant="h5"> Events </Typography>
                <List>
                    {currentEvents.map((event) => (
                        <ListItem
                         key= {event.id}
                         sx={{
                            backgroundColor: colors.greenAccent[500], 
                            margin: "10px 0", 
                            borderRadius:"2px"
                        }} 
                        >
                            <ListItemText
                             primary={event.title}
                             secondary={
                                <Typography>
                                    {formatDate(event.start, {
                                        year : "numeric",
                                        month : "short",
                                        day : "numeric",
                                    })}
                                </Typography>
                             }
                            />
                        </ListItem>
                    ))}
                </List>
            </Box>
        </Box>
    </Box>


};

export default Calendar;
