import nextcord
import config

VIEW_NAME = "LevelRoleView"

#Follow the video to eventually move this to another file because it will be neater
def custom_id(view: str, id: int) -> str:
    #Return the view with the ID
    return f"{config.BOT_NAME}:{view}:{id}"

class LevelRoleView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def handle_click(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        role_id = int(button.custom_id.split(":")[-1])
        role = interaction.guild.get_role(role_id)
        assert isinstance(role, nextcord.Role)
        #if user has the role already
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                f"Your {role.name} role has been removed.",
                ephemeral=True
            )
        #if user doesn't yet have the role
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                f"You've been given the {role.name} role.",
                ephemeral=True
            )

    @nextcord.ui.button(
        label="Beginner",
        emoji = "📖",
        style=nextcord.ButtonStyle.blurple,
        custom_id=custom_id(VIEW_NAME, config.BEGINNER_ROLE_ID),
    )
    async def beginner_role_button(self, button, interaction):
        #await interaction.response.send_message("Clicked Beginner button")
        await self.handle_click(button, interaction)

    @nextcord.ui.button(
        label="Intermediate",
        emoji = "💬",
        style=nextcord.ButtonStyle.red,
        custom_id=custom_id(VIEW_NAME, config.INTERMEDIATE_ROLE_ID),
    )
    async def intermediate_role_button(self, button, interaction):
        #await interaction.response.send_message("Clicked Intermediate button")
        await self.handle_click(button, interaction)
    
    @nextcord.ui.button(
        label="Advanced",
        emoji = "🗺",
        style=nextcord.ButtonStyle.green,
        custom_id=custom_id(VIEW_NAME, config.ADVANCED_ROLE_ID),
    )
    async def advanced_role_button(self, button, interaction):
        #await interaction.response.send_message("Clicked Advanced button")
        await self.handle_click(button, interaction)
    
    @nextcord.ui.button(
        label="Native Speaker",
        emoji = "🕴",
        style=nextcord.ButtonStyle.gray,
        custom_id=custom_id(VIEW_NAME, config.NATIVE_SPEAKER_ROLE_ID),
    )
    async def native_speaker_role_button(self, button, interaction):
        #await interaction.response.send_message("Clicked Native Speaker button")
        await self.handle_click(button, interaction)

#class TestRoleView(nextcord.ui.View):
#    def __init__(self):
#        super().__init__(timeout=None)

#    async def handle_click(self, button:nextcord.ui.Button, interaction:nextcord.Interaction):
#        role_id = int(button.custom_id.split(":")[-1])
#        role = interaction.guild.get_role(role_id)
#        assert isinstance(role, nextcord.role)
#        #if user has the role already
#        if role in interaction.user.roles:
#            await interaction.user.remove_roles(role)
#            await interaction.send.message("Your {role.name} role has been removed.") #later add ,ephermeral=True
        #if user doesn't yet have the role
#        if role in interaction.user.roles:
#            await interaction.user.add_roles(role)
#            await interaction.send.message("You've been given the {role.name} role.")

#    @nextcord.ui.button(
#        label="Test role",
#        emoji = "📖",
#        style=nextcord.ButtonStyle.green, #Don't use .url or .link
#        custom_id=custom_id(VIEW_NAME, config.TEST_ROLE_ID),
#        )
#    async def test_role_button(self, button, interaction):
        #await interaction.response.send_message("Clicked Test role button")
#        await self.handle_click(button, interaction)