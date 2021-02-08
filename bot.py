// Crea il tuo bot passando il token ricevuto da @BotFather 
TelegramBot bot =  new  TelegramBot ( "1459713391:AAHymmVVZxIxVYpoExjJFTR7tx9kSQolYCI" );

// Registrati per il 
bot degli aggiornamenti . setUpdatesListener (aggiornamenti - > {
     // ... aggiornamenti di processo 
    // ritorno id del aggiornamento o confermarle tutte elaborati 
    ritorno  UpdatesListener . CONFIRMED_UPDATES_ALL ;
});

// Invia messaggi 
lunghi chatId = aggiornamento . messaggio () . chat () . id ();
SendResponse response = bot . execute ( new  SendMessage (chatId, " Hello! " ));
