# Maturitni-prace
 Dokumentace a soubory k maturitní práci. 
 
 Cílem mé maturitní práce bylo měření atmosférických dat a ovládání relé pomocí webového rozhraní.  
 
 Cílů jsem dosáhl pomocí dvou mikrokontrolerů, které jsem naprogramoval, aby jeden z nich (ATOM LITE) publikoval data vycházející ze senzoru atmosférických 
 hodnot, byl napojen na reléový modul (SLAVE) a přenášel data pomocí MQTT protokolu na druhý mikrokontroler s displejem (M5stack core).
 
 Tento mikrokontroler sloužil pro vizualizaci dat a zároveň pro ovládání reléového modulu (MASTER), opět pomocí MQTT protokolu. 
 
 Funkce pro posílání skrze MQTT server a ovládání relé modulu byly také vytvořeny ve VSC a jsou použitelné v ostatních systémech podporujících Python.
 
 

