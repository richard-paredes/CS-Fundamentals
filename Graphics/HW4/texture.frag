
#version 330 core
out vec4 color;

in vec2 UV;
uniform sampler2D myTextureSampler;

void main()
{
    // TODO: pub with your code...
    // color = vec4(0.1, 1.0, 0.1, 1.0);
    color = texture(myTextureSampler, UV);
}
