"""
ASBD list of groups needed for applicatiuon business logick
"""

# Povolit mazat i objekty pokud jsou na ne navazana data - napr. Dum pokud obsahuje Byty, nebo prirazane Definice sluzeb
# to by mohl byt ale vzhledem k existujicim uzaverkam veliky prusvih
ALLOW_DELETE_FOREIGN_KEY_CONNECTED_DATA = True

# Group Access Dum Name Suffix
GROUP_ACCESS_DUM_NAME_SUFFIX = "spravce_"
GROUP_CHOICE_FILTER_CONTACTS_SUFFIX = {
    'A': "SVJ",
    'B': "Bytový dům",
}

# Allow/disallow pagination number configuration
ALLOW_USER_PAGINATION_CONFIG = True
