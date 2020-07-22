<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <xsl:for-each select="switches/switch">
            enable
            configure terminal
            !
            hostname <xsl:value-of select="hostname"/>
            !
            <xsl:for-each select="vlans/vlan">
            vlan <xsl:value-of select="number"/>
             name <xsl:value-of select="name"/>
             exit
            !
            </xsl:for-each>
            <xsl:for-each select="interfaces/interface">

            <xsl:choose>
            <xsl:when test="mode='access'">
            int <xsl:value-of select="name"/>
             switchport mode <xsl:value-of select="mode"/>
             switchport access vlan <xsl:value-of select="vlan"/>
             exit
            !
            </xsl:when>
            <xsl:otherwise>
            int <xsl:value-of select="name"/>
             switchport mode <xsl:value-of select="mode"/>
             exit
            !
            </xsl:otherwise>
            </xsl:choose>
            </xsl:for-each>
            exit
            copy running-config startup-config
            
            !
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>