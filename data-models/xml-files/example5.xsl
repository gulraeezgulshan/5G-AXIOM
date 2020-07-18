<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output indent="yes"/>
    <xsl:template match="/">
        <xsl:for-each select="interfaces/interface">
            interface <xsl:value-of select="name"/><br />
            ip address <xsl:value-of select="ipv4addr"/><br />
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>