package main

import (
    "log"
    _"os"
    _"net/http"
    "fmt"
    _"github.com/valyala/fasthttp"
    "database/sql"
    _"github.com/go-sql-driver/mysql"
    "github.com/go-telegram-bot-api/telegram-bot-api"
    "strings"
    "time"
    "strconv"
    "regexp"
)

func conn_db() *sql.DB {
    dbUser := "root"
    dbPassword := "kf"
    dbHost := "localhost"
    dbPort := 3306
    dbName := "KALI000BOT"
    dbProtocol := "tcp"
    db , errDB :=sql.Open("mysql",fmt.Sprintf("%s:%s@%s(%s:%d)/%s",dbUser,dbPassword,dbProtocol,dbHost,dbPort,dbName))
    if errDB != nil{
        log.Fatal(errDB)
    }
    return db 
}

func main() {
    db:=conn_db()
    defer db.Close()
	bot, err := tgbotapi.NewBotAPI("6607140219:AAEO8Yvf0q8su3ue6nZa_-DNyJYjWopE2vM")
	if err != nil {
		log.Fatal(err)
	}
	bot.Debug = false 
	log.Printf("Authorized on account %s", bot.Self.UserName)
	u := tgbotapi.NewUpdate(0)
	u.Timeout = 60
//    updates := bot.ListenForWebhook("/webhook")
//    go fasthttp.ListenAndServe(":8080", func(ctx *fasthttp.RequestCtx) {
//        body := ctx.PostBody()
//        update, err := tgbotapi.NewUpdateFromJSON(body)
//        if err != nil {
//             log.Println(err)
//             ctx.Response.SetStatusCode(fasthttp.StatusBadRequest)
//             return
//        }
//        bot.HandleUpdate(update)
//        ctx.Response.SetStatusCode(fasthttp.StatusOK)
//    })
    updates,err:=bot.GetUpdatesChan(u)
    if err != nil{
        log.Println(err)
    }
    for update := range updates {
        if update.Message == nil {
            continue
        }
        userId := update.Message.From.ID
        userMag := update.Message.Text
        regkey_check_mod1:= `^\w+\s+\w+\s+\d*$`
        regkey_check_mod2:= `^\w+\s+\w`
        isAdmin:=checkAdmin(userId)
        if isAdmin {
            if strings.HasPrefix(userMag,"regkey"){
                check_reg_mod1, err1 := regexp.MatchString(regkey_check_mod1, userMag)
                check_reg_mod2, err2 := regexp.MatchString(regkey_check_mod2, userMag)
                if err1 != nil {
                    log.Println(err1)
                }
                if err2 != nil{
                    log.Println(err2)
                }
                if check_reg_mod1 {
                    list_value:=[]string{}
                    words_regkey:=strings.Fields(userMag)
                    for _,word := range words_regkey{
                        list_value=append(list_value,word)
                    }
                    userName:=list_value[1]
                    dateReg,err:=strconv.Atoi(list_value[2])
                    if err != nil {
                        log.Println(err)
                    }
                    time_st:=time.Now().Format("2006-01-02 15:04")
                    startDate,err:= time.Parse("2006-01-02 15:04", time_st)
                    if err != nil{
                        log.Println(err)
                    }
                    time_en:=startDate.AddDate(0,0,dateReg).Format("2006-01-02 15:04")
                    db:=conn_db()
                    defer db.Close()
                    check_username_c,err:=checkUserName(db,userName)
                    if err != nil {
                        log.Println(err)
                    }
                    if check_username_c {
                        sendMassage(bot,update.Message.Chat.ID,"Sorry, this username is already taken. Please try something different.")
                    }else {
                        err:=registerUser(db,userName,dateReg,time_st,time_en)
                        if err != nil {
                            log.Println(err)
                            continue
                        }else{
                            sendMassage(bot,update.Message.Chat.ID,"An account has been created successfully")
                        }
                    }
                    fmt.Println(userName,"\n",dateReg,time_en)
                }else if check_reg_mod2 {
                    list_value:=[]string{}
                    words_regkey:=strings.Fields(userMag)
                    for _,word := range words_regkey{
                        list_value=append(list_value,word)
                    }
                    userName:=list_value[1]
                    dateReg:=1
                    time_st:=time.Now().Format("2006-1-2 10")
                     startDate,err:= time.Parse("2006-01-02 15:04", time_st)
                    if err != nil{
                        log.Println(err)
                    }
                    time_en:=startDate.AddDate(0,0,dateReg).Format("2006-01-02 15:04")

                    db:=conn_db()
                    defer db.Close()
                    check_username_c,err:=checkUserName(db,userName)
                    if err != nil {
                        log.Println(err)
                    }
                    if check_username_c {
                        sendMassage(bot,update.Message.Chat.ID,"Sorry, this username is already taken. Please try something different.")
                    }else {
                        err:=registerUser(db,userName,dateReg,time_st,time_en)
                        if err != nil {
                            log.Println(err)
                            continue
                        }else {
                        sendMassage(bot,update.Message.Chat.ID,"An account has been created successfully")
                        }
                    }
                }else{
                    sendMassage(bot,update.Message.Chat.ID,"Usage: \nregkey [username] [date]\n date = Day\nexmpale : \n regkey kali01 3 ")
                }
            }
            if strings.HasPrefix(userMag,"info"){
                check_info:= `^\w+\s+\w`
                check_info_mod1, err1 := regexp.MatchString(check_info, userMag)
                if err1 != nil {
                    log.Println(err1)
                }
                if check_info_mod1 {
                    info_list:=[]string{}
                    info_words:=strings.Fields(userMag)
                    for _,word := range(info_words){
                        info_list=append(info_list,word)
                    }
                    username:=info_list[1] 
                    db:=conn_db()
                    defer db.Close()
                    userName,day,time_st,time_en,err,stat:=getInfoUser(db,username)
                    if stat {
                        sendMassage(bot,update.Message.Chat.ID,fmt.Sprintf("Username : %s \nDay : %s\nRecording time : %s\nRegistration_expiration : %s",userName,day,time_st,time_en ))
                        fmt.Println(userName,time_st,day,err)
                    }else {
                        sendMassage(bot,update.Message.Chat.ID,"Not Found user")
                    }
                }
            }else {
                if strings.HasPrefix(userMag,"regkey"){
                } else {
                    sendMassage(bot,update.Message.Chat.ID,"Hi , how are you \nUsage: \ninfo [username] \nregkey user date ")
                }
            }
        }else{
            if strings.HasPrefix(userMag,"regkey") {
                sendMassage(bot,update.Message.Chat.ID,"Sorry ,Permission denied")
            }else if strings.HasPrefix(userMag,"info"){
                 check_info:= `^\w+\s+\w`
                check_info_mod1, err1 := regexp.MatchString(check_info, userMag)
                if err1 != nil {
                    log.Println(err1)
                }
                if check_info_mod1 {
                    info_list:=[]string{}
                    info_words:=strings.Fields(userMag)
                    for _,word := range(info_words){
                        info_list=append(info_list,word)
                    }
                    username:=info_list[1] 
                    db:=conn_db()
                    defer db.Close()
                    userName,day,time_st,time_en,err,stat:=getInfoUser(db,username)
                    if stat {
                        sendMassage(bot,update.Message.Chat.ID,fmt.Sprintf("Username : %s \nDay : %s\nRecording time : %s\nRegistration_expiration : %s",userName,day,time_st,time_en ))
                        fmt.Println(userName,time_st,day,err)
                    }else {
                        sendMassage(bot,update.Message.Chat.ID,"Not Found user")
                    }
                }
            }
        }
	}
}

func checkAdmin(UserId int) bool {
    AdminUserId := int(5594835264)
    if UserId == AdminUserId {
        return true
    }else {
        return false
    }
}

func sendMassage(bot *tgbotapi.BotAPI, chatID int64, message string) {
    msg := tgbotapi.NewMessage(chatID, message)
    _, err := bot.Send(msg)
    if err != nil {
        log.Println(err)
    }
}

func registerUser(db *sql.DB, name string, date int, start_time string ,time_end string) error {
    query := "INSERT INTO USER (USERNAME, DATE, Registration_time,Registration_expiration) VALUES (?, ?, ?,?)"
    _, err := db.Exec(query, name, date, start_time,time_end)
    if err != nil {
        return err
    }
    return nil
}

func checkUserName(db *sql.DB, username_c string) (bool ,error) {
    query := "SELECT COUNT(*) FROM USER WHERE USERNAME = ?"
    var count int
    err := db.QueryRow(query, username_c).Scan(&count)
    if err != nil {
        return false , err
    }
    if count > 0 {
        return true ,nil 
    } else {
        return false, err

    }
}

func getInfoUser(db *sql.DB, name string) (string, string,string, string , error, bool) {
    query := "SELECT * FROM USER WHERE USERNAME = ?"
    var db_name, db_date ,day ,en_date string
    err := db.QueryRow(query, name).Scan(&db_name, &db_date,&day,&en_date)
    if err != nil {
        if err == sql.ErrNoRows {
            return "", "", "","",nil,false
        }
        return "", "", "","",err,false
    }
    return db_name, db_date ,day,en_date,nil,true
}
