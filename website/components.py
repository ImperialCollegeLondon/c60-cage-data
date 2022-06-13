import dash_bootstrap_components as dbc
from dash import dcc


def image_card(src: str, caption: str = None) -> dbc.Card:
    """Generate a card with an image and an optional caption.

    Args:
        src (str): The URL of the image.
        caption (str, optional): The caption describing the image.

    Returns:
        dbc.Card: A card with an image and caption as footer, if provided.
    """
    if caption:
        caption = dbc.CardFooter(caption, style={"text-align": "center"})
    return dbc.Card([dbc.CardImg(src=src, top=True), caption])


def captioned_image_row(images: list) -> dbc.Row:
    """Takes a list of image sources and captions and puts them in a dbc.Row

    Args:
        images (list): A list of dictionaries containing the source and captions for
            the images. The captions are optional. Allowed keywords in dictionary:
                - src: The URL of the image.
                - caption (optional): The caption for the image.


    Returns:
        dbc.Row: A row of images, the number of images is the length of the input list.
    """
    return dbc.Row([dbc.Col(image_card(**im)) for im in images])


def mol_file_upload_button(text: str, id_index: int) -> dbc.Button:
    """A button to upload a mol file. Saves to an in-browser data store.

    Args:
        text (str): The text to display on the button.
        index (int): Index for the id of the button. Must match the index id for the
            mol_image target.

    Returns:
        dbc.Button: A button that will open a file upload dialog.
    """
    return dbc.Button(
        dcc.Upload(text, id=dict(type="mol-file-upload", index=id_index)),
        class_name="me-1",
    )


def _mol_smiles(id_index: int) -> dcc.Store:
    """An intermediate data storage for a smiles string.

    The string is saved here after it is generated from an uploaded mol file.

    Args:
        id_index (int): Index for the id of the Store. Will match its accompanying
            target component.

    Returns:
        dcc.Store: The storage object.
    """
    return dcc.Store(id=dict(type="mol-smiles", index=id_index))


def mol_image(id_index: int, width=3) -> list:
    """A container for a molecule image.

    The container is filled from its accompanying _mol_smiles data store via the
    `display_mol_image` callback.

    Args:
        id_index (int): Index for the component ID - allows for multiple images
        width (optional): Specify the width of the image. Valid arguments are boolean,
            an integer in the range 1-12 inclusive, or a dictionary with keys 'offset',
            'order', 'size'.

    Returns:
        list: List containing the data store and a column to be filled with the image.
    """
    return [
        _mol_smiles(id_index),
        dbc.Col(id=dict(type="mol-image", index=id_index), width=width),
    ]
